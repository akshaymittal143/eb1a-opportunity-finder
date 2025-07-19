# 🚀 EB-1A Opportunity System Deployment Guide

This guide will help you deploy your EB-1A Opportunity System to various platforms.

## 📋 Prerequisites

1. **Email Configuration**: You need a Gmail account with App Password
2. **Git Repository**: Your code should be in a Git repository
3. **Environment Variables**: Configure your `.env` file

## 🔧 Email Setup (Required)

### Gmail App Password Setup
1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Generate an App Password:
   - Go to Security → App Passwords
   - Select "Mail" and your device
   - Copy the generated password

### Environment Variables
Create a `.env` file with:
```bash
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
PORT=5003
```

## 🌐 Deployment Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your repository
3. **Deploy**: Railway will automatically detect and deploy
4. **Set Environment Variables**:
   - Go to your project → Variables
   - Add all variables from your `.env` file
5. **Access**: Your app will be available at `https://your-app.railway.app`

### Option 2: Render (Free Tier Available)

1. **Sign up**: Go to [render.com](https://render.com)
2. **New Web Service**: Connect your GitHub repository
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn src.main:app --bind 0.0.0.0:$PORT`
   - **Environment**: Python 3.11
4. **Environment Variables**: Add all from your `.env` file
5. **Deploy**: Click "Create Web Service"

### Option 3: Heroku

1. **Install Heroku CLI**: `brew install heroku` (macOS)
2. **Login**: `heroku login`
3. **Create App**: `heroku create your-app-name`
4. **Set Config Vars**:
   ```bash
   heroku config:set EMAIL_USERNAME=your-email@gmail.com
   heroku config:set EMAIL_PASSWORD=your-app-password
   heroku config:set SMTP_SERVER=smtp.gmail.com
   heroku config:set SMTP_PORT=587
   ```
5. **Deploy**: `git push heroku main`

### Option 4: Docker Deployment

1. **Build Image**:
   ```bash
   docker build -t eb1a-opportunity-system .
   ```

2. **Run Container**:
   ```bash
   docker run -p 5003:5003 \
     -e EMAIL_USERNAME=your-email@gmail.com \
     -e EMAIL_PASSWORD=your-app-password \
     -e SMTP_SERVER=smtp.gmail.com \
     -e SMTP_PORT=587 \
     eb1a-opportunity-system
   ```

3. **Using Docker Compose**:
   ```bash
   docker-compose up -d
   ```

### Option 5: Local Production Server

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run with Gunicorn**:
   ```bash
   gunicorn src.main:app --bind 0.0.0.0:5003 --workers 4
   ```

3. **Using PM2 (Node.js process manager)**:
   ```bash
   npm install -g pm2
   pm2 start "gunicorn src.main:app --bind 0.0.0.0:5003" --name eb1a-system
   pm2 startup
   pm2 save
   ```

## 🔍 Post-Deployment Verification

1. **Health Check**: Visit `https://your-app.com/api/system/status`
2. **Test Email**: Use the web interface to send a test email
3. **Check Logs**: Monitor application logs for any errors

## 🛠️ Troubleshooting

### Common Issues

1. **Email Not Sending**:
   - Verify Gmail App Password is correct
   - Check SMTP settings
   - Ensure 2FA is enabled on Gmail

2. **Port Issues**:
   - Most platforms use `$PORT` environment variable
   - Update your code to use `os.getenv('PORT', '5003')`

3. **Database Issues**:
   - SQLite works for small deployments
   - For production, consider PostgreSQL

4. **Dependencies**:
   - Ensure `requirements.txt` is up to date
   - Check for platform-specific requirements

### Debug Commands

```bash
# Check application status
curl https://your-app.com/api/system/status

# Test email sending
curl -X POST https://your-app.com/api/test-email \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'

# View logs (platform-specific)
heroku logs --tail
railway logs
```

## 📊 Monitoring

### Health Checks
- **Endpoint**: `/api/system/status`
- **Expected Response**: JSON with system status
- **Monitoring**: Set up uptime monitoring

### Performance
- **Memory**: ~100MB typical usage
- **CPU**: Low usage for email scheduling
- **Storage**: Minimal (SQLite database)

## 🔒 Security Considerations

1. **Environment Variables**: Never commit `.env` files
2. **Email Credentials**: Use App Passwords, not regular passwords
3. **HTTPS**: Enable SSL in production
4. **Rate Limiting**: Consider adding rate limiting for API endpoints

## 📈 Scaling

### For High Traffic
1. **Database**: Migrate to PostgreSQL
2. **Caching**: Add Redis for opportunity caching
3. **Load Balancing**: Use multiple worker processes
4. **CDN**: Serve static files via CDN

### For Multiple Users
1. **Multi-tenancy**: Implement user isolation
2. **Database**: Separate user data
3. **Email Queues**: Use background job processing

## 🎯 Quick Start

1. **Choose Platform**: Railway (easiest) or Render (free)
2. **Connect Repository**: Link your GitHub repo
3. **Set Environment Variables**: Add your email credentials
4. **Deploy**: Platform will handle the rest
5. **Test**: Send a test email via the web interface

## 📞 Support

If you encounter issues:
1. Check the logs for error messages
2. Verify environment variables are set correctly
3. Test email configuration locally first
4. Ensure all dependencies are in `requirements.txt`

---

**🎉 Your EB-1A Opportunity System is now live and ready to help you build your extraordinary ability case!** 