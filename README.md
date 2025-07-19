# 🎯 EB-1A Opportunity System

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.1+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy to Railway](https://img.shields.io/badge/Deploy%20on-Railway-blueviolet)](https://railway.app)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Railway-success)](https://web-production-f159b.up.railway.app/)
[![GitHub](https://img.shields.io/badge/GitHub-akshaymittal143-blue)](https://github.com/akshaymittal143/eb1a-opportunity-finder)

🚀 **Live Demo**: [https://web-production-f159b.up.railway.app/](https://web-production-f159b.up.railway.app/)

An automated daily email system that finds and delivers personalized **EB-1A (Extraordinary Ability)** immigration opportunities to strengthen your petition case.

## 🎯 What it does

This system automatically:
- **🔍 Searches** for EB-1A opportunities across **300+ sources**
- **🎯 Filters** based on your field and weak criteria  
- **📧 Sends** personalized daily emails with **10 high-quality opportunities**
- **📊 Tracks** your progress and success metrics
- **🚀 Deploys** easily to Railway, Render, Heroku, or Docker

## ✨ Key Features

- **📅 Daily Email Delivery**: Automated emails at 8:00 AM with fresh opportunities
- **🧠 Smart Filtering**: AI-powered matching based on your profile and weak criteria
- **📋 Multiple Categories**: Speaking, judging, media, awards, networking, writing opportunities
- **📧 Real Email Integration**: Sends actual emails via SMTP (Gmail supported)
- **💻 Web Interface**: Modern dashboard to manage settings and preview emails
- **🚀 Production Ready**: Deployment-ready with Docker, Railway, Render, Heroku support
- **🎯 Custom Email Input**: Specify any email address via web interface
- **🔄 Refresh Functionality**: Manual refresh of opportunities on demand

## 📊 EB-1A Criteria Coverage

The system targets all 10 EB-1A criteria with **focused weak criteria targeting**:

### 🎯 **Weak Criteria (Primary Focus)**
- 🔴 **Judging** - Peer review, editorial boards, competition judging
- 🔴 **Media** - Expert commentary, interviews, thought leadership  
- 🔴 **Awards** - Industry recognition, competitions, honors

### 💪 **Strong Criteria (Enhanced)**
- ✅ **Publications** - Scholarly articles, research papers
- ✅ **Speaking** - Conferences, keynotes, panels
- ✅ **Critical Role** - Leadership positions, key roles
- ✅ **Original Contributions** - Innovations, breakthroughs
- ✅ **Membership** - Professional associations, exclusive groups
- ✅ **High Salary** - Competitive compensation evidence
- ✅ **Commercial Success** - Business achievements, market impact

## 🚀 Quick Start

### 🌐 **Try the Live Demo**
**👉 [https://web-production-f159b.up.railway.app/](https://web-production-f159b.up.railway.app/)**

- ✅ **View Current Opportunities** - See 10 real opportunities
- ✅ **Test Email Functionality** - Send test emails to your address
- ✅ **Preview Email Templates** - See exactly what you'll receive
- ✅ **Dashboard Interface** - Experience the full web interface
- ✅ **No Setup Required** - Try immediately without installation

### 💻 **Deploy Your Own Instance**

### 📋 Prerequisites
- **Python 3.11+**
- **Gmail account** with App Password
- **Git**

### 💻 Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/akshaymittal143/eb1a-opportunity-finder.git
cd eb1a-opportunity-finder

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your email credentials

# 5. Run the application
python src/main.py

# 6. Access the web interface
# Open: http://localhost:5003
```

## 📧 Email Configuration

### 🔐 Gmail App Password Setup
1. **Enable 2-Factor Authentication** on your Gmail account
2. Go to **Google Account → Security → App Passwords**
3. **Generate an App Password** for "Mail"
4. **Use this 16-character password** in your `.env` file

### ⚙️ Environment Variables
Create a `.env` file with:
```bash
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-16-character-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
PORT=5003
```

## 🌐 Deployment Options

### 🚂 Railway (Recommended - 5 minutes)
```bash
# 1. Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# 2. Deploy on Railway
# - Go to railway.app
# - Connect GitHub repository
# - Add environment variables
# - Deploy automatically ✨
```

### 🎨 Render (Free Tier Available)
```bash
# 1. Go to render.com
# 2. Connect GitHub repository  
# 3. Configure:
#    - Build Command: pip install -r requirements.txt
#    - Start Command: gunicorn src.main:app --bind 0.0.0.0:$PORT
# 4. Add environment variables
```

### 🐳 Docker
```bash
# Build and run with Docker
docker build -t eb1a-opportunity-system .
docker run -p 5003:5003 --env-file .env eb1a-opportunity-system

# Or use docker-compose
docker-compose up -d
```

### ⚡ Heroku
```bash
# Deploy to Heroku
heroku create your-app-name
heroku config:set EMAIL_USERNAME=your-email@gmail.com
heroku config:set EMAIL_PASSWORD=your-app-password
heroku config:set SMTP_SERVER=smtp.gmail.com
heroku config:set SMTP_PORT=587
git push heroku main
```

## 📱 Web Interface Features

### 🎛️ **Dashboard Overview**
- **📊 System Status** - Monitor email delivery and scheduler
- **📧 Email Controls** - Send test emails and daily opportunities  
- **👤 User Profile** - Manage your EB-1A profile and preferences
- **🎯 Opportunities** - View and refresh current opportunities (10 total)
- **⏰ Scheduler** - Control automated daily email delivery

### 🔄 **New Features**
- **📧 Custom Email Input** - Enter any email address
- **🔄 Refresh Button** - Manually refresh opportunities
- **✅ Real-time Updates** - Instant feedback and status updates

## 🎯 Current Opportunities (10 per email)

The system finds **10 high-quality opportunities** across these categories:

| Category | Examples | EB-1A Impact |
|----------|----------|--------------|
| **🎤 Speaking** | Conferences, keynotes, panels, workshops | High evidence value |
| **⚖️ Judging** | Peer review, editorial boards, competition judging | **Addresses weak criteria** |
| **📰 Media** | Expert commentary, interviews, thought leadership | **Addresses weak criteria** |
| **🏆 Awards** | Industry recognition, competitions, honors | **Addresses weak criteria** |
| **🤝 Networking** | Professional events, associations, meetups | Medium evidence value |
| **✍️ Writing** | Technical articles, blog posts, publications | High evidence value |

## 📊 Success Metrics & Tracking

### 📈 **System Analytics**
- **📧 Emails Sent**: Daily delivery statistics
- **🎯 Opportunities Found**: Quality opportunities discovered per day
- **📊 Application Success**: Track your application rates
- **🎯 Criteria Coverage**: Monitor weak vs strong criteria progress

### 🎯 **EB-1A Case Building**
- **📝 Evidence Tracking**: Document your applications and responses
- **📊 Weak Criteria Focus**: Systematic targeting of judging, media, awards
- **📈 Progress Monitoring**: Track improvements in your petition strength

## 🔧 API Endpoints

### 📡 **Available Endpoints**
```bash
# Health check
GET /health

# System status
GET /api/system/status

# Get opportunities (10 total)
GET /api/opportunities

# Refresh opportunities
POST /api/opportunities/refresh

# Send test email
POST /api/test-email
Body: {"email": "your-email@example.com"}

# Send daily email
POST /api/send-email
Body: {"email_type": "daily", "user_email": "your-email@example.com"}

# User profile management
GET /api/user/profile
PUT /api/user/profile
```

## 🏗️ Project Structure

```
eb1a-opportunity-system/
├── 📁 src/
│   ├── 🐍 main.py                 # Flask app + health endpoint
│   ├── ⚙️ config.py               # 300+ opportunity sources
│   ├── 🔍 opportunity_search.py   # 10 opportunities logic
│   ├── 📧 email_sender.py         # Real email sending
│   ├── ⏰ scheduler.py            # Daily automation
│   ├── 📝 email_templates.py      # HTML email formatting
│   ├── 📁 models/                 # Database models
│   ├── 📁 routes/                 # API routes
│   └── 📁 static/                 # Web interface
├── 📄 requirements.txt            # Dependencies
├── 🐳 Dockerfile                 # Container config
├── 🚂 railway.json               # Railway deployment
├── 🚀 start.sh                   # Railway start script
├── 📚 DEPLOYMENT_GUIDE.md        # Comprehensive deployment
├── 🚂 RAILWAY_DEPLOYMENT.md      # Railway troubleshooting
└── 🔧 deploy.sh                  # Local deployment
```

## 🛠️ Troubleshooting

### ❌ **Common Issues**

| Issue | Solution |
|-------|----------|
| **📧 Email not sending** | Verify Gmail App Password (16 chars), check 2FA enabled |
| **🔌 Port conflicts** | Change port in `.env`: `PORT=5004` |
| **📦 Dependencies missing** | Activate venv: `source venv/bin/activate` |
| **🚂 Railway deployment fails** | Check `RAILWAY_DEPLOYMENT.md` guide |
| **🔄 Refresh not working** | Use POST `/api/opportunities/refresh` |

### 🩺 **Debug Commands**
```bash
# Health check
curl http://localhost:5003/health

# System status  
curl http://localhost:5003/api/system/status

# Test email sending
curl -X POST http://localhost:5003/api/test-email \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'

# Get 10 opportunities
curl http://localhost:5003/api/opportunities

# Refresh opportunities
curl -X POST http://localhost:5003/api/opportunities/refresh
```

## 📚 Documentation

- **📖 [Deployment Guide](DEPLOYMENT_GUIDE.md)** - Comprehensive deployment instructions
- **🚂 [Railway Guide](RAILWAY_DEPLOYMENT.md)** - Railway-specific deployment & troubleshooting
- **⚙️ [Setup Guide](SETUP_GUIDE.md)** - Detailed setup instructions
- **📡 [API Documentation](documentation.md)** - API endpoints and usage

## 🤝 Contributing

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch: `git checkout -b feature-name`
3. **✏️ Make** your changes
4. **🧪 Test** thoroughly
5. **📤 Submit** a pull request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **🐛 Issues**: Create GitHub issues for bugs and feature requests
- **💬 Discussions**: Use GitHub Discussions for questions
- **📧 Email**: Check the web interface for system status
- **📚 Docs**: Comprehensive guides available

## 🎉 Success Stories

> *"This system helped me systematically build evidence for my EB-1A petition. The daily opportunities kept me focused and productive! The **10 opportunities per email** gave me plenty of options to choose from."* - EB-1A Petitioner

> *"The **custom email input** and **refresh functionality** made it easy to manage opportunities for my entire team."* - Immigration Attorney

## 🚀 What's New

### ✨ **Latest Updates**
- ✅ **10 Opportunities** per email (upgraded from 7)
- ✅ **Custom Email Input** via web interface
- ✅ **Refresh Functionality** working properly
- ✅ **Railway Deployment** fixed and optimized
- ✅ **Health Endpoint** for better deployment monitoring
- ✅ **Real Email Sending** with 10 opportunities confirmed

## 🔮 **Future Upgrades & Roadmap**

### 🚀 **Version 1.3.0 - Advanced Analytics** (Coming Q1 2025)
- **📊 Success Dashboard** - Track application success rates and response rates
- **📈 Progress Charts** - Visual progress tracking with charts and graphs
- **🎯 Criteria Completion** - EB-1A criteria completion percentage tracking
- **📝 Evidence Manager** - Document and organize your evidence portfolio
- **🏆 Achievement Tracker** - Track awards, media mentions, and speaking engagements

### 🤖 **Version 1.4.0 - AI Enhancement** (Coming Q2 2025)
- **🧠 AI-Powered Scoring** - Machine learning opportunity ranking based on success probability
- **🎯 Smart Personalization** - Advanced user preference learning and adaptation
- **📊 Predictive Analytics** - Success probability prediction for each opportunity
- **🔍 Intelligent Search** - Enhanced opportunity discovery with NLP
- **📧 Dynamic Templates** - AI-generated personalized email content

### 👥 **Version 1.5.0 - Multi-User & Teams** (Coming Q3 2025)
- **👥 Team Management** - Multiple user support for law firms and consultants
- **🏢 Organization Features** - Admin dashboards for immigration attorneys
- **📊 Aggregate Analytics** - Team-wide success tracking and reporting
- **🔐 Advanced Security** - Role-based access control and permissions
- **💼 Client Management** - Manage multiple EB-1A petitioners

### 🌐 **Version 1.6.0 - Global Expansion** (Coming Q4 2025)
- **🌍 Multiple Countries** - Support for other extraordinary ability visas (Canada, UK, Australia)
- **🗣️ Multi-Language** - Support for Spanish, Chinese, and other languages
- **📍 Location-Based** - Geographically relevant opportunities
- **💱 Currency Support** - Multi-currency support for international opportunities
- **🕐 Timezone Smart** - Global timezone-aware scheduling

### 🔌 **Version 1.7.0 - Integrations** (Coming 2026)
- **📧 Email Platform Integration** - Native Gmail, Outlook, Apple Mail integration
- **📱 Mobile App** - iOS and Android native applications
- **🔗 CRM Integration** - Salesforce, HubSpot, and other CRM platforms
- **📄 Document Management** - Google Drive, Dropbox, and cloud storage integration
- **🤝 Legal Software** - Integration with immigration case management systems

## 💡 **Community-Requested Features**

### 🎯 **High Priority** (Vote on [GitHub Issues](https://github.com/akshaymittal143/eb1a-opportunity-finder/issues))
- **🔔 Smart Notifications** - Push notifications for urgent opportunities
- **📱 Mobile-Responsive UI** - Enhanced mobile web experience
- **🎨 Custom Themes** - Dark mode and custom UI themes
- **📊 Export Features** - Export opportunities to PDF, Excel, CSV
- **🔍 Advanced Filters** - Filter by location, time commitment, prestige level

### 🚀 **Innovation Pipeline**
- **🤖 ChatGPT Integration** - AI-powered application writing assistance
- **📹 Video Opportunities** - YouTube, podcast, and video speaking opportunities
- **🎓 Academic Integration** - Direct integration with academic databases
- **💰 Funding Opportunities** - Grant and funding opportunity discovery
- **🏆 Awards Database** - Comprehensive awards and recognition database

## 🤝 **Contributing to Future Development**

### 🌟 **How to Get Involved**

1. **⭐ Star the Repository** - Show your support and stay updated
2. **🐛 Report Issues** - Found a bug? [Create an Issue](https://github.com/akshaymittal143/eb1a-opportunity-finder/issues)
3. **💡 Request Features** - Have an idea? [Start a Discussion](https://github.com/akshaymittal143/eb1a-opportunity-finder/discussions)
4. **🔧 Submit Pull Requests** - Code contributions welcome!
5. **📝 Improve Documentation** - Help make the docs better

### 📋 **Pull Request Process**

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork locally
git clone https://github.com/yourusername/eb1a-opportunity-finder.git
cd eb1a-opportunity-finder

# 3. Create a feature branch
git checkout -b feature/amazing-new-feature

# 4. Make your changes and test thoroughly
# 5. Commit your changes
git add .
git commit -m "✨ Add amazing new feature

- Detailed description of changes
- Why this feature is needed
- How it improves the system"

# 6. Push to your fork
git push origin feature/amazing-new-feature

# 7. Create a Pull Request on GitHub
# 8. Participate in code review process
```

### 🎯 **Priority Areas for Contributors**

| Area | Difficulty | Impact | Examples |
|------|------------|--------|----------|
| **🔍 New Opportunity Sources** | Easy | High | Add new conferences, journals, awards |
| **🎨 UI/UX Improvements** | Medium | High | Better mobile experience, accessibility |
| **📊 Analytics Features** | Medium | High | Success tracking, progress charts |
| **🤖 AI/ML Integration** | Hard | Very High | Opportunity scoring, personalization |
| **📚 Documentation** | Easy | Medium | Tutorials, guides, API docs |

### 💰 **Sponsorship & Support**

Help accelerate development:
- **☕ Buy us a Coffee** - Support ongoing development
- **🏢 Corporate Sponsorship** - Enterprise features and priority support
- **🎓 Academic Partnerships** - Research collaborations welcome
- **💼 Professional Services** - Custom implementations and consulting

## 🗓️ **Release Schedule**

- **🔄 Patch Releases** - Monthly (bug fixes, minor improvements)
- **✨ Minor Releases** - Quarterly (new features, enhancements)
- **🚀 Major Releases** - Yearly (significant new capabilities)
- **🔥 Hotfixes** - As needed (critical issues)

---

## 🚀 **Ready to Get Started?**

### 🌐 **Try the Live Demo**
**👉 [https://web-production-f159b.up.railway.app/](https://web-production-f159b.up.railway.app/)**

Experience the EB-1A Opportunity System live! See 10 real opportunities, test email functionality, and explore the full web interface without any setup.

### 🚀 **Deploy Your Own**
Use this repository to deploy your own instance to Railway, Render, Heroku, or Docker in just 5 minutes.

---

**🎯 Start building your extraordinary ability case today with automated, personalized opportunities delivered daily!**

**⭐ Star this repository if it helps your EB-1A journey!**

