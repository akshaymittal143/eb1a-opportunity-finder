import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp

# Import our EB-1A system components
from src.config import SystemConfig, create_default_user_profile, validate_config
from src.opportunity_search import OpportunitySearcher
from src.email_sender import EmailSender, MockEmailSender
from src.scheduler import OpportunityScheduler, SchedulerManager
from src.email_templates import EmailPersonalizer, HTMLEmailGenerator

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'asdf#FGSgvasgf$5$WGT')

# Enable CORS for all routes
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')

# Database configuration - support both local and production
database_url = os.getenv('DATABASE_URL', f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}")
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# Initialize EB-1A system components
scheduler_manager = SchedulerManager()
user_profile = create_default_user_profile()

# Add default user scheduler (using mock email for demo)
default_scheduler = scheduler_manager.add_user_scheduler("default", user_profile, use_mock_email=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

# EB-1A API Routes

@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    """Get current opportunities for the user"""
    try:
        searcher = OpportunitySearcher(user_profile.__dict__)
        opportunities = searcher.search_all_opportunities()
        filtered_opportunities = searcher.filter_opportunities(opportunities)
        
        # Convert opportunities to dict format
        opportunities_data = []
        for opp in filtered_opportunities:
            opportunities_data.append({
                "title": opp.title,
                "type": opp.type.value,
                "description": opp.description,
                "deadline": opp.deadline,
                "link": opp.link,
                "prestige_rating": opp.prestige_rating,
                "evidence_value": opp.evidence_value,
                "time_investment": opp.time_investment,
                "why_fits": opp.why_fits,
                "keywords": opp.keywords,
                "date_found": opp.date_found
            })
        
        return jsonify({
            "opportunities": opportunities_data,
            "count": len(opportunities_data),
            "last_updated": "2025-07-19T10:00:00Z"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/send-email', methods=['POST'])
def send_email():
    """Manually trigger email sending"""
    try:
        data = request.get_json()
        email_type = data.get('email_type', 'daily')
        user_email = data.get('user_email', user_profile.email)
        
        scheduler = scheduler_manager.get_scheduler("default")
        if not scheduler:
            return jsonify({"error": "Scheduler not found"}), 404
        
        success = scheduler.run_now(email_type)
        
        if success:
            return jsonify({
                "message": f"{email_type.title()} email sent successfully",
                "email": user_email,
                "type": email_type
            })
        else:
            return jsonify({"error": "Failed to send email"}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    """Get current user profile"""
    try:
        return jsonify({
            "name": user_profile.name,
            "email": user_profile.email,
            "field": user_profile.field,
            "role": user_profile.role,
            "location": user_profile.location,
            "weak_criteria": user_profile.weak_criteria,
            "strong_criteria": user_profile.strong_criteria,
            "keywords": user_profile.keywords,
            "notification_frequency": user_profile.notification_frequency.value,
            "email_format": user_profile.email_format.value,
            "max_opportunities_per_email": user_profile.max_opportunities_per_email,
            "timezone": user_profile.timezone
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/user/profile', methods=['PUT'])
def update_user_profile():
    """Update user profile"""
    try:
        data = request.get_json()
        
        # Update profile fields
        if 'name' in data:
            user_profile.name = data['name']
        if 'email' in data:
            user_profile.email = data['email']
        if 'notification_frequency' in data:
            from src.config import NotificationFrequency
            user_profile.notification_frequency = NotificationFrequency(data['notification_frequency'])
        if 'max_opportunities_per_email' in data:
            user_profile.max_opportunities_per_email = int(data['max_opportunities_per_email'])
        
        # Update scheduler with new profile
        scheduler = scheduler_manager.get_scheduler("default")
        if scheduler:
            scheduler.update_user_profile(user_profile)
        
        return jsonify({"message": "Profile updated successfully"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/system/status', methods=['GET'])
def get_system_status():
    """Get system status and statistics"""
    try:
        # Validate configuration
        config_validation = validate_config()
        
        # Get scheduler statistics
        scheduler = scheduler_manager.get_scheduler("default")
        scheduler_stats = scheduler.get_stats() if scheduler else {}
        next_runs = scheduler.get_next_run_times() if scheduler else {}
        
        return jsonify({
            "system_status": "running",
            "configuration": {
                "email_config": config_validation.get("email_config", False),
                "database_config": config_validation.get("database_config", False),
                "user_profile": config_validation.get("user_profile", False),
                "errors": config_validation.get("errors", [])
            },
            "scheduler": {
                "running": scheduler.is_running if scheduler else False,
                "stats": scheduler_stats,
                "next_runs": next_runs
            },
            "version": "1.0.0",
            "last_updated": "2025-07-19"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test-email', methods=['POST'])
def test_email():
    """Send a test email to verify configuration"""
    try:
        data = request.get_json()
        test_email = data.get('email', user_profile.email)
        
        # Use mock sender for testing
        sender = MockEmailSender()
        success = sender.send_test_email(test_email)
        
        if success:
            sent_emails = sender.get_sent_emails()
            return jsonify({
                "message": "Test email sent successfully",
                "email": test_email,
                "mock_email_data": sent_emails[-1] if sent_emails else None
            })
        else:
            return jsonify({"error": "Failed to send test email"}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/preview-email', methods=['GET'])
def preview_email():
    """Preview email content without sending"""
    try:
        email_type = request.args.get('type', 'daily')
        format_type = request.args.get('format', 'html')
        
        # Get opportunities
        searcher = OpportunitySearcher(user_profile.__dict__)
        opportunities = searcher.search_all_opportunities()
        filtered_opportunities = searcher.filter_opportunities(opportunities)
        
        if email_type == 'daily':
            if format_type == 'html':
                content = HTMLEmailGenerator.generate_html_daily_email(
                    filtered_opportunities, user_profile.__dict__
                )
                return content, 200, {'Content-Type': 'text/html'}
            else:
                personalizer = EmailPersonalizer(user_profile.__dict__)
                content = personalizer.personalize_daily_email(filtered_opportunities)
                return content, 200, {'Content-Type': 'text/plain'}
        
        return jsonify({"error": "Invalid email type or format"}), 400
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/scheduler/start', methods=['POST'])
def start_scheduler():
    """Start the scheduler"""
    try:
        scheduler = scheduler_manager.get_scheduler("default")
        if scheduler:
            scheduler.start()
            return jsonify({"message": "Scheduler started successfully"})
        else:
            return jsonify({"error": "Scheduler not found"}), 404
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/scheduler/stop', methods=['POST'])
def stop_scheduler():
    """Stop the scheduler"""
    try:
        scheduler = scheduler_manager.get_scheduler("default")
        if scheduler:
            scheduler.stop()
            return jsonify({"message": "Scheduler stopped successfully"})
        else:
            return jsonify({"error": "Scheduler not found"}), 404
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the default scheduler
    default_scheduler.start()
    
    print("=== EB-1A Opportunity System ===")
    print("System starting up...")
    print(f"User: {user_profile.name} ({user_profile.email})")
    print(f"Notification frequency: {user_profile.notification_frequency.value}")
    print("Web interface available at: http://localhost:5000")
    print("API documentation: http://localhost:5000/api/system/status")
    
    # Production-ready configuration
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
