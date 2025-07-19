# 🚀 Quick Start - Deploy in 5 Minutes

## Option 1: Railway (Easiest - Free)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect and deploy

3. **Add Environment Variables**
   In Railway dashboard, add these variables:
   ```
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_USERNAME=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   FROM_EMAIL=your-email@gmail.com
   USER_NAME="Your Name"
   USER_EMAIL=your-email@gmail.com
   USER_FIELD="Your field"
   USER_ROLE="Your role"
   USER_LOCATION="Your location"
   WEAK_CRITERIA=judging,media,awards
   STRONG_CRITERIA=publications,speaking,critical role
   USER_KEYWORDS=AI,ML,Cloud Native,DevSecOps,Cybersecurity
   NOTIFICATION_FREQUENCY=daily
   EMAIL_FORMAT=html
   MAX_OPPORTUNITIES=7
   USER_TIMEZONE=America/Chicago
   SECRET_KEY=your-secret-key
   ```

4. **Done!** Your app will be live at `https://your-app.railway.app`

## Option 2: Render (Free Tier)

1. **Go to [render.com](https://render.com)**
2. **Sign up with GitHub**
3. **Create Web Service**
   - Connect your GitHub repo
   - Name: `eb1a-opportunity-system`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python src/main.py`
4. **Add environment variables** (same as Railway above)
5. **Deploy**

## Option 3: Local Development

```bash
# Run the deployment script
./deploy.sh

# Or manually:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## 🔧 Email Setup (Required for Real Emails)

### Gmail Setup:
1. Enable 2-Factor Authentication
2. Generate App Password:
   - Google Account → Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this 16-character password in `EMAIL_PASSWORD`

### Test Email:
1. Visit your deployed app
2. Go to "Send Test Email"
3. Enter your email address
4. Check if email is received

## 🎯 What You Get

- **Daily Opportunity Emails**: Personalized opportunities for EB-1A petition
- **Web Dashboard**: Manage settings and preview emails
- **API Endpoints**: Programmatic access to opportunities
- **Email Templates**: Professional HTML and text emails
- **Scheduling**: Automated daily delivery

## 📊 System Features

- **Opportunity Search**: Finds speaking, judging, media, awards opportunities
- **Smart Filtering**: Prioritizes your weak EB-1A criteria
- **Email Personalization**: Customized content based on your profile
- **Progress Tracking**: Monitor your application success rate
- **Web Interface**: Real-time dashboard and controls

## 🚨 Troubleshooting

**App won't start:**
- Check environment variables are set
- Verify Python 3.11+ is installed
- Check logs for error messages

**Email not sending:**
- Verify SMTP credentials
- Check app password is correct
- Test with mock email first

**Need help:**
- Check `/api/system/status` endpoint
- Review logs in platform dashboard
- Test locally first

## 📞 Support

- **Documentation**: `README.md` and `documentation.md`
- **Deployment Guide**: `DEPLOYMENT_GUIDE.md`
- **API Status**: Visit `/api/system/status` on your deployed app

Your EB-1A Opportunity System is now live! 🎉 