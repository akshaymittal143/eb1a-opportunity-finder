#!/bin/bash

# EB-1A Opportunity System Deployment Script
# This script helps you deploy your application to various platforms

set -e

echo "🚀 EB-1A Opportunity System Deployment"
echo "======================================"

# Check if we're in the right directory
if [ ! -f "src/main.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | sed 's/Python //' | cut -d. -f1,2)
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Error: Python 3.11+ required, found $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
./venv/bin/python -m pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: No .env file found"
    echo "📝 Creating sample .env file..."
    cat > .env << EOF
# Email Configuration (Required for real email sending)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
FROM_EMAIL=your-email@gmail.com

# User Profile
USER_NAME="Your Name"
USER_EMAIL=your-email@example.com
USER_FIELD="Software Engineer, AI/ML research"
USER_ROLE="Full Stack Software Engineer, PhD Student"
USER_LOCATION="Your Location"
WEAK_CRITERIA=judging,media,awards
STRONG_CRITERIA=publications,speaking,critical role
USER_KEYWORDS=AI,ML,Cloud Native,DevSecOps,Cybersecurity

# System Settings
NOTIFICATION_FREQUENCY=daily
EMAIL_FORMAT=html
MAX_OPPORTUNITIES=7
USER_TIMEZONE=America/Chicago
SECRET_KEY=your-secret-key-here
EOF
    echo "📝 Please edit .env file with your actual settings"
fi

# Test the application
echo "🧪 Testing application..."
./venv/bin/python src/main.py &
APP_PID=$!

# Wait for app to start
sleep 5

# Test health endpoint
if curl -s http://localhost:5000/api/system/status > /dev/null; then
    echo "✅ Application test successful"
else
    echo "❌ Application test failed"
    kill $APP_PID 2>/dev/null || true
    exit 1
fi

# Stop test server
kill $APP_PID 2>/dev/null || true

echo ""
echo "🎉 Setup complete! Your application is ready for deployment."
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your email settings"
echo "2. Choose a deployment platform:"
echo "   - Railway (easiest): https://railway.app"
echo "   - Render (free): https://render.com"
echo "   - Heroku: https://heroku.com"
echo "3. Follow the deployment guide in DEPLOYMENT_GUIDE.md"
echo ""
echo "🔧 To run locally:"
echo "   python src/main.py"
echo ""
echo "🌐 Access at: http://localhost:5000" 