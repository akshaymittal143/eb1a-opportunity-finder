"""
EB-1A Opportunity Scheduler Module
Handles automated scheduling of daily emails and system tasks
"""

import schedule
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, Any, Callable, Optional
import logging
import json
import os

from src.config import SystemConfig, UserProfile, NotificationFrequency, create_default_user_profile
from src.opportunity_search import OpportunitySearcher
from src.email_sender import EmailSender, MockEmailSender
from src.email_templates import EmailPersonalizer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpportunityScheduler:
    """Handles scheduling of opportunity emails and system tasks"""
    
    def __init__(self, user_profile: UserProfile = None, use_mock_email: bool = False):
        self.user_profile = user_profile or create_default_user_profile()
        
        print(f"DEBUG: use_mock_email={use_mock_email}")
        if use_mock_email:
            print("DEBUG: Using MockEmailSender")
            self.email_sender = MockEmailSender()
        else:
            print("DEBUG: Using EmailSender")
            self.email_sender = EmailSender()
        
        self.opportunity_searcher = OpportunitySearcher(self.user_profile.__dict__)
        self.is_running = False
        self.scheduler_thread = None
        
        # Statistics tracking
        self.stats = {
            "emails_sent": 0,
            "opportunities_found": 0,
            "last_run": None,
            "errors": 0,
            "start_time": datetime.now().isoformat()
        }
        
        self._setup_schedule()
    
    def _setup_schedule(self):
        """Setup the scheduling based on user preferences"""
        schedule.clear()  # Clear any existing schedules
        
        if self.user_profile.notification_frequency == NotificationFrequency.DAILY:
            # Schedule daily email at 8:00 AM user's timezone
            schedule.every().day.at("08:00").do(self._send_daily_opportunities)
            logger.info("Scheduled daily opportunities email at 8:00 AM")
            
        elif self.user_profile.notification_frequency == NotificationFrequency.WEEKLY:
            # Schedule weekly email on Monday at 8:00 AM
            schedule.every().monday.at("08:00").do(self._send_weekly_summary)
            logger.info("Scheduled weekly summary email on Mondays at 8:00 AM")
        
        # Schedule system maintenance tasks
        schedule.every().day.at("02:00").do(self._daily_maintenance)
        schedule.every().hour.do(self._check_urgent_opportunities)
        
        logger.info(f"Scheduler configured for {self.user_profile.notification_frequency.value} notifications")
    
    def _send_daily_opportunities(self):
        """Send daily opportunities email"""
        try:
            logger.info("Starting daily opportunities email generation")
            logger.info(f"DEBUG: max_opportunities_per_email = {self.user_profile.max_opportunities_per_email}")
            
            # Search for opportunities
            opportunities = self.opportunity_searcher.search_all_opportunities()
            filtered_opportunities = self.opportunity_searcher.filter_opportunities(
                opportunities, 
                max_count=self.user_profile.max_opportunities_per_email
            )
            
            if not filtered_opportunities:
                logger.warning("No opportunities found for daily email")
                return
            
            # Send email
            success = self.email_sender.send_daily_opportunities_email(
                self.user_profile, 
                filtered_opportunities
            )
            
            if success:
                self.stats["emails_sent"] += 1
                self.stats["opportunities_found"] += len(filtered_opportunities)
                self.stats["last_run"] = datetime.now().isoformat()
                logger.info(f"Daily opportunities email sent successfully with {len(filtered_opportunities)} opportunities")
            else:
                self.stats["errors"] += 1
                logger.error("Failed to send daily opportunities email")
                
        except Exception as e:
            self.stats["errors"] += 1
            logger.error(f"Error in daily opportunities task: {str(e)}")
    
    def _send_weekly_summary(self):
        """Send weekly summary email"""
        try:
            logger.info("Starting weekly summary email generation")
            
            # This would typically pull from a database of tracked opportunities
            # For now, we'll send a basic summary
            
            subject = f"Weekly EB-1A Summary - {datetime.now().strftime('%Y-%m-%d')}"
            content = f"""
Weekly EB-1A Opportunity Summary

Dear {self.user_profile.name},

Here's your weekly summary:

📊 This Week's Stats:
- Opportunities identified: {self.stats.get('opportunities_found', 0)}
- Emails sent: {self.stats.get('emails_sent', 0)}
- System uptime: {self._get_uptime()}

🎯 Focus Areas:
Your weak criteria that need attention: {', '.join(self.user_profile.weak_criteria)}

💡 Tip of the Week:
Consistency is key in building your EB-1A case. Small, regular actions compound into significant achievements.

Keep up the excellent work!

Your EB-1A Opportunity System
            """
            
            success = self.email_sender.send_email(
                to_email=self.user_profile.email,
                subject=subject,
                plain_content=content
            )
            
            if success:
                self.stats["emails_sent"] += 1
                self.stats["last_run"] = datetime.now().isoformat()
                logger.info("Weekly summary email sent successfully")
            else:
                self.stats["errors"] += 1
                logger.error("Failed to send weekly summary email")
                
        except Exception as e:
            self.stats["errors"] += 1
            logger.error(f"Error in weekly summary task: {str(e)}")
    
    def _check_urgent_opportunities(self):
        """Check for urgent opportunities with tight deadlines"""
        try:
            logger.debug("Checking for urgent opportunities")
            
            opportunities = self.opportunity_searcher.search_all_opportunities()
            
            # Filter for urgent opportunities (deadline within 3 days)
            urgent_opportunities = []
            for opp in opportunities:
                if self._is_urgent_deadline(opp.deadline):
                    urgent_opportunities.append(opp)
            
            if urgent_opportunities:
                logger.info(f"Found {len(urgent_opportunities)} urgent opportunities")
                
                # Send urgent notification for the highest-rated opportunity
                top_urgent = self.opportunity_searcher.filter_opportunities(
                    urgent_opportunities, max_count=1
                )
                
                if top_urgent:
                    success = self.email_sender.send_urgent_opportunity_email(
                        self.user_profile, 
                        top_urgent[0]
                    )
                    
                    if success:
                        self.stats["emails_sent"] += 1
                        logger.info("Urgent opportunity email sent")
                    else:
                        self.stats["errors"] += 1
                        logger.error("Failed to send urgent opportunity email")
            
        except Exception as e:
            logger.error(f"Error checking urgent opportunities: {str(e)}")
    
    def _daily_maintenance(self):
        """Perform daily maintenance tasks"""
        try:
            logger.info("Running daily maintenance")
            
            # Clear old cache files
            cache_dir = SystemConfig.CACHE_DIRECTORY
            if os.path.exists(cache_dir):
                for filename in os.listdir(cache_dir):
                    file_path = os.path.join(cache_dir, filename)
                    if os.path.isfile(file_path):
                        # Remove files older than cache duration
                        file_age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))
                        if file_age > timedelta(hours=SystemConfig.CACHE_DURATION_HOURS):
                            os.remove(file_path)
                            logger.debug(f"Removed old cache file: {filename}")
            
            # Save statistics
            self._save_stats()
            
            logger.info("Daily maintenance completed")
            
        except Exception as e:
            logger.error(f"Error in daily maintenance: {str(e)}")
    
    def _is_urgent_deadline(self, deadline_str: str) -> bool:
        """Check if a deadline is urgent (within 3 days)"""
        try:
            # Simple heuristic - look for date patterns
            # In a real implementation, this would parse various date formats
            urgent_keywords = ["today", "tomorrow", "urgent", "asap"]
            deadline_lower = deadline_str.lower()
            
            return any(keyword in deadline_lower for keyword in urgent_keywords)
            
        except Exception:
            return False
    
    def _get_uptime(self) -> str:
        """Get system uptime as a formatted string"""
        try:
            start_time = datetime.fromisoformat(self.stats["start_time"])
            uptime = datetime.now() - start_time
            
            days = uptime.days
            hours, remainder = divmod(uptime.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            
            return f"{days}d {hours}h {minutes}m"
            
        except Exception:
            return "Unknown"
    
    def _save_stats(self):
        """Save statistics to file"""
        try:
            stats_file = "scheduler_stats.json"
            with open(stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2)
            logger.debug("Statistics saved")
            
        except Exception as e:
            logger.error(f"Failed to save statistics: {str(e)}")
    
    def start(self):
        """Start the scheduler in a separate thread"""
        if self.is_running:
            logger.warning("Scheduler is already running")
            return
        
        self.is_running = True
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        logger.info("Scheduler started")
    
    def stop(self):
        """Stop the scheduler"""
        self.is_running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)
        logger.info("Scheduler stopped")
    
    def _run_scheduler(self):
        """Main scheduler loop"""
        logger.info("Scheduler loop started")
        
        while self.is_running:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                logger.error(f"Error in scheduler loop: {str(e)}")
                time.sleep(60)  # Continue after error
        
        logger.info("Scheduler loop ended")
    
    def run_now(self, task_name: str = "daily") -> bool:
        """Manually trigger a scheduled task"""
        try:
            if task_name == "daily":
                self._send_daily_opportunities()
                return True
            elif task_name == "weekly":
                self._send_weekly_summary()
                return True
            elif task_name == "urgent":
                self._check_urgent_opportunities()
                return True
            elif task_name == "maintenance":
                self._daily_maintenance()
                return True
            else:
                logger.error(f"Unknown task: {task_name}")
                return False
                
        except Exception as e:
            logger.error(f"Error running task {task_name}: {str(e)}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get current statistics"""
        return self.stats.copy()
    
    def get_next_run_times(self) -> Dict[str, str]:
        """Get next scheduled run times"""
        next_runs = {}
        
        for job in schedule.jobs:
            job_name = job.job_func.__name__
            next_run = job.next_run
            if next_run:
                next_runs[job_name] = next_run.strftime("%Y-%m-%d %H:%M:%S")
        
        return next_runs
    
    def update_user_profile(self, new_profile: UserProfile):
        """Update user profile and reschedule tasks"""
        self.user_profile = new_profile
        self.opportunity_searcher = OpportunitySearcher(new_profile.__dict__)
        self._setup_schedule()
        logger.info("User profile updated and schedule reconfigured")

class SchedulerManager:
    """Manages multiple schedulers and provides a unified interface"""
    
    def __init__(self):
        self.schedulers: Dict[str, OpportunityScheduler] = {}
    
    def add_user_scheduler(self, user_id: str, user_profile: UserProfile, 
                          use_mock_email: bool = False) -> OpportunityScheduler:
        """Add a scheduler for a specific user"""
        scheduler = OpportunityScheduler(user_profile, use_mock_email)
        self.schedulers[user_id] = scheduler
        return scheduler
    
    def remove_user_scheduler(self, user_id: str):
        """Remove a user's scheduler"""
        if user_id in self.schedulers:
            self.schedulers[user_id].stop()
            del self.schedulers[user_id]
    
    def start_all(self):
        """Start all schedulers"""
        for scheduler in self.schedulers.values():
            scheduler.start()
    
    def stop_all(self):
        """Stop all schedulers"""
        for scheduler in self.schedulers.values():
            scheduler.stop()
    
    def get_scheduler(self, user_id: str) -> Optional[OpportunityScheduler]:
        """Get a specific user's scheduler"""
        return self.schedulers.get(user_id)
    
    def get_all_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get statistics for all schedulers"""
        return {user_id: scheduler.get_stats() 
                for user_id, scheduler in self.schedulers.items()}

if __name__ == "__main__":
    # Test the scheduler
    print("=== Testing Opportunity Scheduler ===")
    
    # Create test user profile
    user_profile = create_default_user_profile()
    user_profile.name = "Test User"
    user_profile.email = "test@example.com"
    
    # Create scheduler with mock email
    scheduler = OpportunityScheduler(user_profile, use_mock_email=True)
    
    print(f"Scheduler created for {user_profile.name}")
    print(f"Notification frequency: {user_profile.notification_frequency.value}")
    
    # Test manual task execution
    print("\nTesting manual task execution:")
    
    success = scheduler.run_now("daily")
    print(f"Daily task: {'✓' if success else '✗'}")
    
    success = scheduler.run_now("weekly")
    print(f"Weekly task: {'✓' if success else '✗'}")
    
    success = scheduler.run_now("urgent")
    print(f"Urgent check: {'✓' if success else '✗'}")
    
    success = scheduler.run_now("maintenance")
    print(f"Maintenance: {'✓' if success else '✗'}")
    
    # Show statistics
    stats = scheduler.get_stats()
    print(f"\nScheduler Statistics:")
    print(f"Emails sent: {stats['emails_sent']}")
    print(f"Opportunities found: {stats['opportunities_found']}")
    print(f"Errors: {stats['errors']}")
    print(f"Uptime: {scheduler._get_uptime()}")
    
    # Show next run times
    next_runs = scheduler.get_next_run_times()
    print(f"\nNext scheduled runs:")
    for task, time_str in next_runs.items():
        print(f"  {task}: {time_str}")
    
    # Test scheduler manager
    print(f"\n=== Testing Scheduler Manager ===")
    
    manager = SchedulerManager()
    test_scheduler = manager.add_user_scheduler("test_user", user_profile, use_mock_email=True)
    
    print(f"Added scheduler for test_user")
    
    all_stats = manager.get_all_stats()
    print(f"All stats: {all_stats}")
    
    # Clean up
    manager.stop_all()
    print("All schedulers stopped")

