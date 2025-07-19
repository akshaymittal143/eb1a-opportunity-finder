# 🚂 Railway Deployment Guide - EB-1A Opportunity System

## 🚀 Quick Railway Deployment

### Step 1: Prepare Your Repository
Make sure these files are in your repository:
- `railway.json` ✅
- `requirements.txt` ✅
- `start.sh` ✅
- `Procfile` ✅
- `src/main.py` ✅

### Step 2: Deploy to Railway

1. **Go to Railway**: [railway.app](https://railway.app)
2. **Login with GitHub**
3. **New Project** → **Deploy from GitHub repo**
4. **Select your repository**

### Step 3: Configure Environment Variables

In Railway dashboard → **Variables**, add:

```bash
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-16-character-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Step 4: Monitor Deployment

1. Watch the **Deploy Logs** tab
2. Check for successful health check at `/health`
3. Once deployed, test the endpoints

## 🔧 Troubleshooting Railway Issues

### Issue 1: Healthcheck Failure ❌

**Symptoms**: "Healthcheck failure" in logs

**Solutions**:
1. **Check Environment Variables**: Ensure all required variables are set
2. **Health Endpoint**: Visit `https://your-app.railway.app/health`
3. **System Status**: Try `https://your-app.railway.app/api/system/status`

### Issue 2: App Won't Start ❌

**Symptoms**: "Build succeeded but deploy failed"

**Solutions**:
1. **Check Build Logs**: Look for Python/dependency errors
2. **Start Command**: Railway should use `bash start.sh`
3. **Port Configuration**: Railway automatically sets `$PORT`

### Issue 3: Email Not Working ❌

**Symptoms**: App starts but emails fail

**Solutions**:
1. **Gmail App Password**: 
   - Enable 2FA on Gmail
   - Generate App Password (16 characters)
   - Use this instead of regular password
2. **Test Endpoint**: `POST /api/test-email`
3. **Check Variables**: Verify EMAIL_USERNAME and EMAIL_PASSWORD

### Issue 4: Database Errors ❌

**Symptoms**: SQLite or database related errors

**Solutions**:
1. **File System**: Railway provides ephemeral storage
2. **Database Migration**: The start script handles table creation
3. **Persistent Storage**: For production, consider Railway's database addon

## 🧪 Testing Your Deployment

### 1. Health Check
```bash
curl https://your-app.railway.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-07-19T17:30:00Z",
  "version": "1.0.0"
}
```

### 2. System Status
```bash
curl https://your-app.railway.app/api/system/status
```

### 3. Test Email
```bash
curl -X POST https://your-app.railway.app/api/test-email \
  -H "Content-Type: application/json" \
  -d '{"email": "your-email@gmail.com"}'
```

### 4. Send Daily Email
```bash
curl -X POST https://your-app.railway.app/api/send-email \
  -H "Content-Type: application/json" \
  -d '{"email_type": "daily", "user_email": "your-email@gmail.com"}'
```

## 📊 Railway Configuration Details

### Current Setup:
- **Builder**: Nixpacks (auto-detected)
- **Start Command**: `bash start.sh`
- **Health Check**: `/health` endpoint
- **Workers**: 2 Gunicorn workers
- **Timeout**: 120 seconds

### Environment Variables Required:
- `EMAIL_USERNAME` - Your Gmail address
- `EMAIL_PASSWORD` - Gmail App Password (16 chars)
- `SMTP_SERVER` - smtp.gmail.com
- `SMTP_PORT` - 587

### Optional Variables:
- `PORT` - Set automatically by Railway
- `FLASK_ENV` - production (default)

## 🔍 Common Railway Logs

### ✅ Successful Deployment
```
🚀 Starting EB-1A Opportunity System on Railway...
🗄️ Setting up database...
✅ Database setup complete
🔥 Starting web server...
[gunicorn] Starting gunicorn 21.2.0
[gunicorn] Listening at: http://0.0.0.0:xxxx
```

### ❌ Failed Deployment Examples

**Missing Environment Variables:**
```
ERROR: EMAIL_USERNAME not found
```
**Solution**: Add EMAIL_USERNAME in Railway Variables

**Port Issues:**
```
[ERROR] connection in use
```
**Solution**: Railway handles ports automatically

**Database Issues:**
```
SQLite error: disk I/O error
```
**Solution**: Railway's filesystem is ephemeral - this is normal

## 🎯 Post-Deployment Steps

1. **Test the Web Interface**: Visit your Railway URL
2. **Configure Email**: Enter your email in the interface
3. **Send Test Email**: Verify email delivery works
4. **Set Daily Schedule**: Emails will be sent at 8:00 AM daily

## 📞 Getting Help

1. **Railway Docs**: [docs.railway.app](https://docs.railway.app)
2. **Check Logs**: Deploy Logs and HTTP Logs tabs
3. **Health Check**: Use `/health` endpoint for quick status
4. **Discord**: Railway has an active Discord community

## 🔄 Redeployment

If you make changes:
1. **Push to GitHub**: `git push origin main`
2. **Railway Auto-deploys**: Watches your repository
3. **Check Deploy Logs**: Monitor the deployment
4. **Test Health**: Verify `/health` endpoint

---

**🎉 Once deployed successfully, your EB-1A Opportunity System will be live and sending you daily opportunities to build your extraordinary ability case!** 