# EB-1A Opportunity System - Deployment Guide

This guide provides step-by-step instructions for deploying your EB-1A Opportunity System to various platforms.

## 🚀 Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)

**Time to deploy: 5 minutes**

1. **Sign up for Railway** (free tier available)
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   ```bash
   # Push your code to GitHub first
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

3. **Connect to Railway**
   - In Railway dashboard, click "New Project"
   - Choose "Deploy from GitHub repo"
   - Select your repository

4. **Configure Environment Variables**
   Add these in Railway dashboard:
   ```
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_USERNAME=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   FROM_EMAIL=your-email@gmail.com
   USER_NAME="Your Name"
   USER_EMAIL=your-email@gmail.com
   USER_FIELD="Your field description"
   USER_ROLE="Your role"
   USER_LOCATION="Your location"
   WEAK_CRITERIA=judging,media,awards
   STRONG_CRITERIA=publications,speaking,critical role
   USER_KEYWORDS=AI,ML,Cloud Native,DevSecOps,Cybersecurity
   NOTIFICATION_FREQUENCY=daily
   EMAIL_FORMAT=html
   MAX_OPPORTUNITIES=7
   USER_TIMEZONE=America/Chicago
   SECRET_KEY=your-secret-key-here
   ```

5. **Deploy**
   - Railway will automatically detect the Python app
   - It will use the `railway.json` configuration
   - Your app will be live in minutes

### Option 2: Render (Free Tier Available)

**Time to deploy: 10 minutes**

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create a Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure the service:**
   - **Name**: `eb1a-opportunity-system`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python src/main.py`
   - **Plan**: Free

4. **Add Environment Variables** (same as Railway above)

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically

### Option 3: Heroku (Paid)

**Time to deploy: 15 minutes**

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # Download from heroku.com
   ```

2. **Login and create app**
   ```bash
   heroku login
   heroku create your-eb1a-app-name
   ```

3. **Configure environment variables**
   ```bash
   heroku config:set SMTP_SERVER=smtp.gmail.com
   heroku config:set SMTP_PORT=587
   heroku config:set EMAIL_USERNAME=your-email@gmail.com
   heroku config:set EMAIL_PASSWORD=your-app-password
   # ... add all other variables
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Option 4: DigitalOcean App Platform

**Time to deploy: 20 minutes**

1. **Create DigitalOcean account**
2. **Go to App Platform**
3. **Connect GitHub repository**
4. **Configure build settings:**
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `python src/main.py`
5. **Add environment variables**
6. **Deploy**

## 🔧 Advanced Deployment Options

### Option 5: AWS EC2 (Full Control)

**Time to deploy: 30 minutes**

1. **Launch EC2 instance**
   ```bash
   # Ubuntu 22.04 LTS recommended
   # t3.micro (free tier) or t3.small
   ```

2. **Connect and install dependencies**
   ```bash
   ssh ubuntu@your-ec2-ip
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

3. **Deploy application**
   ```bash
   git clone your-repo
   cd eb1a-opportunity-system
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set up systemd service**
   ```bash
   sudo nano /etc/systemd/system/eb1a.service
   ```
   
   Add this content:
   ```ini
   [Unit]
   Description=EB-1A Opportunity System
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/eb1a-opportunity-system
   Environment="PATH=/home/ubuntu/eb1a-opportunity-system/venv/bin"
   ExecStart=/home/ubuntu/eb1a-opportunity-system/venv/bin/python src/main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

5. **Start the service**
   ```bash
   sudo systemctl enable eb1a
   sudo systemctl start eb1a
   ```

6. **Configure Nginx** (optional)
   ```bash
   sudo nano /etc/nginx/sites-available/eb1a
   ```
   
   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### Option 6: Docker Deployment

**Time to deploy: 25 minutes**

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 5000
   CMD ["python", "src/main.py"]
   ```

2. **Build and run**
   ```bash
   docker build -t eb1a-system .
   docker run -p 5000:5000 --env-file .env eb1a-system
   ```

3. **Deploy to Docker Hub**
   ```bash
   docker tag eb1a-system your-username/eb1a-system
   docker push your-username/eb1a-system
   ```

## 🔐 Security Considerations

### Environment Variables
- **Never commit sensitive data** to your repository
- Use environment variables for all configuration
- Rotate secrets regularly

### Email Security
- Use app passwords, not your main password
- Enable 2FA on your email account
- Consider using a dedicated email for the system

### Database Security
- For production, use PostgreSQL instead of SQLite
- Enable SSL connections
- Regular backups

## 📊 Monitoring and Maintenance

### Health Checks
Your app includes a health check endpoint:
```
GET /api/system/status
```

### Logs
- Railway: View logs in dashboard
- Render: Logs tab in dashboard
- Heroku: `heroku logs --tail`
- EC2: `sudo journalctl -u eb1a -f`

### Updates
1. Update your code
2. Push to GitHub
3. Platform will auto-deploy (Railway, Render)
4. Or manually deploy: `git push heroku main`

## 🚨 Troubleshooting

### Common Issues

**App won't start:**
- Check environment variables are set
- Verify Python version (3.11+)
- Check logs for error messages

**Email not sending:**
- Verify SMTP credentials
- Check if app password is correct
- Test with mock email first

**Database errors:**
- Ensure database directory exists
- Check file permissions
- For production, use PostgreSQL

### Getting Help
1. Check the logs first
2. Test locally: `python src/main.py`
3. Verify environment variables
4. Check the `/api/system/status` endpoint

## 🎯 Next Steps After Deployment

1. **Test the system**
   - Visit your live URL
   - Send a test email
   - Check system status

2. **Configure email settings**
   - Set up real SMTP credentials
   - Test email delivery

3. **Customize your profile**
   - Update keywords for your field
   - Adjust notification frequency
   - Set your weak/strong criteria

4. **Monitor performance**
   - Check system status regularly
   - Monitor email delivery
   - Track opportunity quality

## 📞 Support

- **Documentation**: Check `README.md` and `documentation.md`
- **Issues**: Create GitHub issues for bugs
- **Questions**: Check the web interface `/api/system/status`

Your EB-1A Opportunity System is now ready to help strengthen your petition! 🚀 