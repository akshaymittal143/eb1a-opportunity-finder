# EB-1A Opportunity System - Complete Setup Guide

This guide will walk you through setting up your own EB-1A Opportunity System for automated daily emails with personalized opportunities.

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.11 or higher** installed on your system
2. **Email account** with SMTP access (Gmail, Outlook, etc.)
3. **Basic command line knowledge**
4. **Text editor** for configuration files

## 🚀 Step-by-Step Installation

### Step 1: Download the System

You can either:
- Download the complete system files from the provided source
- Or clone from a repository if available

### Step 2: Set Up Python Environment

```bash
# Navigate to the project directory
cd eb1a-opportunity-system

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### Step 3: Configure Email Settings

#### For Gmail Users:
1. **Enable 2-Factor Authentication** on your Google account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
   - Copy the 16-character password

#### For Other Email Providers:
- **Outlook/Hotmail**: Use `smtp.live.com`, port 587
- **Yahoo**: Use `smtp.mail.yahoo.com`, port 587
- **Custom SMTP**: Contact your email provider for settings

### Step 4: Create Configuration File

Create a `.env` file in the project root directory:

```bash
# Email Configuration (REQUIRED for real email sending)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-16-character-app-password
FROM_EMAIL=your-email@gmail.com

# Your Personal Information
USER_NAME="Dr. Alex Chen"
USER_EMAIL=your-email@gmail.com
USER_FIELD="Software Engineer, AI/ML research in Cloud Native, DevSecOps, Cybersecurity"
USER_ROLE="Full Stack Software Engineer, doing AI/ML research as PhD Student"
USER_LOCATION="Austin, Texas, or Remote anywhere"

# EB-1A Criteria (customize based on your strengths/weaknesses)
WEAK_CRITERIA=judging,media,awards
STRONG_CRITERIA=publications,speaking,critical role

# Your Expertise Keywords (customize for your field)
USER_KEYWORDS=AI,ML,Machine Learning,Cloud Native,DevSecOps,Cybersecurity,Software Engineering

# System Preferences
NOTIFICATION_FREQUENCY=daily
EMAIL_FORMAT=html
MAX_OPPORTUNITIES=7
USER_TIMEZONE=America/Chicago
```

### Step 5: Test the System

#### Test 1: Basic Functionality
```bash
# Test opportunity search
python src/opportunity_search.py

# Expected output: List of 7-8 opportunities with ratings
```

#### Test 2: Email Templates
```bash
# Test email formatting
PYTHONPATH=/path/to/eb1a-opportunity-system python src/email_templates.py

# Expected output: Sample email content in text and HTML
```

#### Test 3: Email Sending (Mock)
```bash
# Test email sender with mock
PYTHONPATH=/path/to/eb1a-opportunity-system python src/email_sender.py

# Expected output: Mock emails sent successfully
```

### Step 6: Start the System

```bash
# Start the web application
python src/main.py
```

You should see:
```
=== EB-1A Opportunity System ===
System starting up...
User: Dr. Alex Chen (your-email@gmail.com)
Notification frequency: daily
Web interface available at: http://localhost:5000
API documentation: http://localhost:5000/api/system/status
```

### Step 7: Access the Web Interface

1. Open your browser and go to `http://localhost:5000`
2. You should see the EB-1A Opportunity System dashboard
3. Test the following features:
   - **System Status**: Check if all components are working
   - **Send Test Email**: Verify email configuration
   - **Preview Email**: See how your daily emails will look
   - **Current Opportunities**: View today's opportunities

## 🔧 Configuration Options

### Email Frequency Settings

```bash
# Daily emails (recommended)
NOTIFICATION_FREQUENCY=daily

# Weekly summary only
NOTIFICATION_FREQUENCY=weekly

# Urgent opportunities only
NOTIFICATION_FREQUENCY=urgent_only
```

### Email Format Options

```bash
# HTML emails (recommended)
EMAIL_FORMAT=html

# Plain text emails
EMAIL_FORMAT=plain_text

# Both formats
EMAIL_FORMAT=both
```

### Customizing Your Profile

Edit these settings in your `.env` file:

```bash
# Adjust based on your EB-1A petition status
WEAK_CRITERIA=judging,media,awards,membership
STRONG_CRITERIA=publications,speaking,critical role,original contributions

# Add your specific expertise areas
USER_KEYWORDS=AI,ML,Deep Learning,Computer Vision,NLP,Kubernetes,Docker,Security,DevOps

# Set your preferred number of opportunities per email
MAX_OPPORTUNITIES=5  # For fewer opportunities
MAX_OPPORTUNITIES=10 # For more opportunities
```

## 📧 Setting Up Automated Daily Emails

### Option 1: Keep the Application Running
- The system automatically sends emails when running
- Daily emails at 8:00 AM in your timezone
- Urgent alerts for time-sensitive opportunities

### Option 2: Schedule with System Cron (Linux/macOS)
```bash
# Add to your crontab
crontab -e

# Add this line for daily 8 AM emails
0 8 * * * cd /path/to/eb1a-opportunity-system && python src/scheduler.py --run-once
```

### Option 3: Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for daily at 8:00 AM
4. Set action to run: `python /path/to/eb1a-opportunity-system/src/scheduler.py --run-once`

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### 1. Email Not Sending
**Problem**: "Email configuration incomplete" or authentication errors

**Solutions**:
- Verify your email credentials in `.env` file
- For Gmail: Ensure you're using an App Password, not your regular password
- Check SMTP server and port settings
- Test with the mock email sender first

#### 2. No Opportunities Found
**Problem**: System returns empty opportunity list

**Solutions**:
- Check your keywords in `USER_KEYWORDS`
- Verify internet connection
- Review the opportunity sources in `config.py`
- Try broadening your keyword list

#### 3. Import Errors
**Problem**: "ModuleNotFoundError" when running scripts

**Solutions**:
```bash
# Set Python path explicitly
export PYTHONPATH=/path/to/eb1a-opportunity-system
# Or use:
PYTHONPATH=/path/to/eb1a-opportunity-system python src/script_name.py
```

#### 4. Web Interface Not Loading
**Problem**: Cannot access http://localhost:5000

**Solutions**:
- Check if the application is running
- Verify no other application is using port 5000
- Try accessing http://127.0.0.1:5000 instead
- Check firewall settings

#### 5. Scheduler Not Working
**Problem**: Daily emails not being sent automatically

**Solutions**:
- Verify the scheduler is started (check web interface)
- Check system logs for errors
- Ensure the application stays running
- Verify timezone settings

### Debug Mode

Enable debug logging:
```bash
# Set environment variable
export LOG_LEVEL=DEBUG

# Run the application
python src/main.py
```

## 📊 Monitoring Your Success

### Track Your Progress
The system automatically tracks:
- **Opportunities Found**: Total relevant opportunities identified
- **Emails Sent**: Number of daily/weekly emails delivered
- **Response Rate**: Your application success rate (manual tracking)
- **Criteria Coverage**: How well opportunities address your weak areas

### Monthly Review
1. Check your email statistics in the web interface
2. Review which types of opportunities you've pursued
3. Update your profile based on new achievements
4. Adjust keywords and criteria as needed

## 🔄 Regular Maintenance

### Weekly Tasks
- Review and update your profile if needed
- Check system status for any errors
- Clear old log files if disk space is limited

### Monthly Tasks
- Update your keywords based on new expertise
- Review and adjust weak/strong criteria
- Update your location or contact information
- Backup your configuration files

### System Updates
- Check for updates to the opportunity sources
- Update Python packages: `pip install --upgrade -r requirements.txt`
- Review and update email templates if needed

## 🚀 Advanced Configuration

### Adding Custom Opportunity Sources
1. Edit `src/opportunity_search.py`
2. Add new search methods for your preferred sources
3. Update the opportunity categories in `src/config.py`

### Custom Email Templates
1. Modify templates in `src/email_templates.py`
2. Customize HTML styling in the email generator
3. Add new email types (weekly, monthly, etc.)

### Integration with Other Tools
- **Calendar Integration**: Add deadlines to your calendar
- **CRM Integration**: Track applications and follow-ups
- **Analytics**: Export data for detailed analysis

## 📞 Getting Help

### Self-Help Resources
1. **System Status**: Check `/api/system/status` for diagnostics
2. **Logs**: Review application logs for error messages
3. **Documentation**: Refer to `documentation.md` for detailed information

### Community Support
- Share your configuration challenges
- Report bugs or suggest improvements
- Contribute to the project development

## 🎯 Success Tips

### Maximizing Your Results
1. **Be Specific**: Use precise keywords for your expertise
2. **Stay Consistent**: Check and respond to opportunities regularly
3. **Track Everything**: Document your applications and outcomes
4. **Network Actively**: Use opportunities to build professional relationships
5. **Quality Over Quantity**: Focus on high-impact opportunities

### EB-1A Petition Strategy
1. **Address Weak Criteria First**: Prioritize judging, media, and awards
2. **Document Impact**: Keep detailed records of your contributions
3. **Build Relationships**: Networking leads to future opportunities
4. **Stay Persistent**: Consistent effort compounds over time

---

**Congratulations!** 🎉 

You now have a fully functional EB-1A Opportunity System that will help strengthen your extraordinary ability petition with daily, personalized opportunities.

**Next Steps:**
1. ✅ Complete the setup following this guide
2. ✅ Send your first test email
3. ✅ Review your first daily opportunity email
4. ✅ Start applying to relevant opportunities
5. ✅ Track your progress and success rate

**Remember**: Building a strong EB-1A case takes time and consistency. This system will help you stay on track with daily opportunities tailored to your expertise and petition needs.

Good luck with your EB-1A journey! 🚀

