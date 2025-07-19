"""
EB-1A Email Sender Module
Handles email delivery using SMTP
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Optional, Dict, Any
import logging
from datetime import datetime
import os

from src.config import SystemConfig, UserProfile, EmailFormat
from src.opportunity_search import Opportunity
from src.email_templates import EmailPersonalizer, HTMLEmailGenerator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailSender:
    """Handles email sending functionality"""
    
    def __init__(self, smtp_server: str = None, smtp_port: int = None, 
                 username: str = None, password: str = None):
        self.smtp_server = smtp_server or SystemConfig.SMTP_SERVER
        self.smtp_port = smtp_port or SystemConfig.SMTP_PORT
        self.username = username or SystemConfig.EMAIL_USERNAME
        self.password = password or SystemConfig.EMAIL_PASSWORD
        self.from_email = SystemConfig.FROM_EMAIL or self.username
        
        # Validate configuration
        if not all([self.smtp_server, self.username, self.password]):
            logger.warning("Email configuration incomplete. Email sending will be disabled.")
            self.enabled = False
        else:
            self.enabled = True
    
    def send_daily_opportunities_email(self, user_profile: UserProfile, 
                                     opportunities: List[Opportunity]) -> bool:
        """Send daily opportunities email to user"""
        try:
            if not self.enabled:
                logger.warning("Email sending is disabled due to incomplete configuration")
                return False
            
            # Generate email content
            personalizer = EmailPersonalizer(user_profile.__dict__)
            
            if user_profile.email_format in [EmailFormat.HTML, EmailFormat.BOTH]:
                html_content = HTMLEmailGenerator.generate_html_daily_email(
                    opportunities, user_profile.__dict__
                )
            else:
                html_content = None
            
            if user_profile.email_format in [EmailFormat.PLAIN_TEXT, EmailFormat.BOTH]:
                plain_content = personalizer.personalize_daily_email(opportunities)
            else:
                plain_content = None
            
            # Send email
            subject = f"Daily EB-1A Opportunities - {datetime.now().strftime('%Y-%m-%d')}"
            
            return self.send_email(
                to_email=user_profile.email,
                subject=subject,
                plain_content=plain_content,
                html_content=html_content
            )
            
        except Exception as e:
            logger.error(f"Failed to send daily opportunities email: {str(e)}")
            return False
    
    def send_urgent_opportunity_email(self, user_profile: UserProfile, 
                                    opportunity: Opportunity) -> bool:
        """Send urgent opportunity notification"""
        try:
            if not self.enabled:
                logger.warning("Email sending is disabled")
                return False
            
            subject = f"🚨 URGENT: High-Value EB-1A Opportunity - Deadline {opportunity.deadline}"
            
            plain_content = f"""
URGENT OPPORTUNITY ALERT

{opportunity.title}

Description: {opportunity.description}
Deadline: {opportunity.deadline}
Link: {opportunity.link}

Why this is perfect for you: {opportunity.why_fits}

Don't miss this opportunity to strengthen your EB-1A petition!

Time remaining: Please check the deadline carefully.

Your EB-1A Opportunity System
            """.strip()
            
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .urgent {{ background-color: #ff4444; color: white; padding: 20px; text-align: center; }}
        .opportunity {{ background-color: #f9f9f9; padding: 20px; margin: 20px 0; border-left: 5px solid #ff4444; }}
        .link {{ color: #007cba; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="urgent">
        <h1>🚨 URGENT OPPORTUNITY ALERT</h1>
        <p>High-value opportunity with tight deadline!</p>
    </div>
    
    <div class="opportunity">
        <h2>{opportunity.title}</h2>
        <p><strong>Description:</strong> {opportunity.description}</p>
        <p><strong>Deadline:</strong> {opportunity.deadline}</p>
        <p><strong>Why it fits:</strong> {opportunity.why_fits}</p>
        <p><a href="{opportunity.link}" class="link">Apply Now →</a></p>
    </div>
    
    <p>Don't miss this opportunity to strengthen your EB-1A petition!</p>
    
    <hr>
    <p><small>Your EB-1A Opportunity System</small></p>
</body>
</html>
            """
            
            return self.send_email(
                to_email=user_profile.email,
                subject=subject,
                plain_content=plain_content,
                html_content=html_content
            )
            
        except Exception as e:
            logger.error(f"Failed to send urgent opportunity email: {str(e)}")
            return False
    
    def send_test_email(self, to_email: str) -> bool:
        """Send a test email to verify configuration"""
        try:
            if not self.enabled:
                return False
            
            subject = "EB-1A Opportunity System - Test Email"
            plain_content = """
This is a test email from your EB-1A Opportunity System.

If you received this email, your email configuration is working correctly!

System Status:
- Email sending: ✓ Working
- SMTP server: Connected
- Authentication: Successful

Your EB-1A Opportunity System is ready to send you daily opportunities.

Best regards,
EB-1A Opportunity System
            """.strip()
            
            html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .header { background-color: #4CAF50; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .status { background-color: #e8f5e8; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>✅ Test Email Successful</h1>
        <p>EB-1A Opportunity System</p>
    </div>
    
    <div class="content">
        <p>This is a test email from your EB-1A Opportunity System.</p>
        
        <div class="status">
            <h3>System Status:</h3>
            <ul>
                <li>✅ Email sending: Working</li>
                <li>✅ SMTP server: Connected</li>
                <li>✅ Authentication: Successful</li>
            </ul>
        </div>
        
        <p>Your EB-1A Opportunity System is ready to send you daily opportunities.</p>
        
        <p>Best regards,<br>EB-1A Opportunity System</p>
    </div>
</body>
</html>
            """
            
            return self.send_email(
                to_email=to_email,
                subject=subject,
                plain_content=plain_content,
                html_content=html_content
            )
            
        except Exception as e:
            logger.error(f"Failed to send test email: {str(e)}")
            return False
    
    def send_email(self, to_email: str, subject: str, 
                   plain_content: str = None, html_content: str = None,
                   attachments: List[str] = None) -> bool:
        """Send email with optional HTML content and attachments"""
        try:
            if not self.enabled:
                logger.warning("Email sending is disabled")
                return False
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add plain text content
            if plain_content:
                msg.attach(MIMEText(plain_content, 'plain'))
            
            # Add HTML content
            if html_content:
                msg.attach(MIMEText(html_content, 'html'))
            
            # Add attachments
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                        
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename= {os.path.basename(file_path)}'
                        )
                        msg.attach(part)
            
            # Create secure connection and send email
            context = ssl.create_default_context()
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.username, self.password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return False
    
    def validate_configuration(self) -> Dict[str, Any]:
        """Validate email configuration"""
        validation_result = {
            "valid": False,
            "errors": [],
            "warnings": []
        }
        
        # Check required configuration
        if not self.smtp_server:
            validation_result["errors"].append("SMTP server not configured")
        
        if not self.username:
            validation_result["errors"].append("Email username not configured")
        
        if not self.password:
            validation_result["errors"].append("Email password not configured")
        
        if validation_result["errors"]:
            return validation_result
        
        # Test connection
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.username, self.password)
            
            validation_result["valid"] = True
            logger.info("Email configuration validated successfully")
            
        except smtplib.SMTPAuthenticationError:
            validation_result["errors"].append("SMTP authentication failed - check username/password")
        except smtplib.SMTPConnectError:
            validation_result["errors"].append("Failed to connect to SMTP server")
        except Exception as e:
            validation_result["errors"].append(f"Email configuration error: {str(e)}")
        
        return validation_result

class MockEmailSender(EmailSender):
    """Mock email sender for testing purposes"""
    
    def __init__(self):
        self.enabled = True
        self.sent_emails = []
    
    def send_email(self, to_email: str, subject: str, 
                   plain_content: str = None, html_content: str = None,
                   attachments: List[str] = None) -> bool:
        """Mock email sending - stores emails instead of sending"""
        email_record = {
            "to": to_email,
            "subject": subject,
            "plain_content": plain_content,
            "html_content": html_content,
            "attachments": attachments or [],
            "timestamp": datetime.now().isoformat()
        }
        
        self.sent_emails.append(email_record)
        logger.info(f"Mock email sent to {to_email}: {subject}")
        return True
    
    def get_sent_emails(self) -> List[Dict[str, Any]]:
        """Get list of sent emails for testing"""
        return self.sent_emails
    
    def clear_sent_emails(self):
        """Clear sent emails list"""
        self.sent_emails = []

if __name__ == "__main__":
    # Test email sender
    from src.opportunity_search import OpportunitySearcher, create_user_profile
    from src.config import create_default_user_profile
    
    print("=== Testing Email Sender ===")
    
    # Use mock sender for testing
    sender = MockEmailSender()
    
    # Create test data
    user_profile = create_default_user_profile()
    user_profile.email = "test@example.com"
    
    searcher = OpportunitySearcher(user_profile.__dict__)
    opportunities = searcher.search_all_opportunities()
    filtered_opportunities = searcher.filter_opportunities(opportunities)
    
    # Test daily email
    success = sender.send_daily_opportunities_email(user_profile, filtered_opportunities)
    print(f"Daily email sent: {'✓' if success else '✗'}")
    
    # Test urgent email
    if filtered_opportunities:
        urgent_opp = filtered_opportunities[0]
        success = sender.send_urgent_opportunity_email(user_profile, urgent_opp)
        print(f"Urgent email sent: {'✓' if success else '✗'}")
    
    # Test test email
    success = sender.send_test_email("test@example.com")
    print(f"Test email sent: {'✓' if success else '✗'}")
    
    # Show sent emails
    sent_emails = sender.get_sent_emails()
    print(f"\nTotal emails sent: {len(sent_emails)}")
    
    for i, email in enumerate(sent_emails, 1):
        print(f"{i}. To: {email['to']}")
        print(f"   Subject: {email['subject']}")
        print(f"   Timestamp: {email['timestamp']}")
    
    # Test real email sender validation (without sending)
    real_sender = EmailSender()
    validation = real_sender.validate_configuration()
    print(f"\nReal email configuration valid: {'✓' if validation['valid'] else '✗'}")
    if validation['errors']:
        print(f"Errors: {validation['errors']}")

