#!/bin/bash

# EB-1A Opportunity System - GitHub Setup Script

echo "🚀 Setting up EB-1A Opportunity System for GitHub..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already exists"
fi

# Create .env from example if it doesn't exist
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "📄 Creating .env file from .env.example..."
        cp .env.example .env
        echo "⚠️  Please edit .env file with your actual email credentials!"
    else
        echo "⚠️  .env.example not found. Please create .env manually."
    fi
else
    echo "✅ .env file already exists"
fi

# Add all files to git
echo "📦 Adding files to Git..."
git add .

# Create initial commit if needed
if [ -z "$(git log --oneline 2>/dev/null)" ]; then
    echo "💾 Creating initial commit..."
    git commit -m "Initial commit: EB-1A Opportunity System

✨ Features:
- 📧 Daily emails with 10 high-quality opportunities
- 🎯 Targets weak EB-1A criteria (judging, media, awards)
- 🔍 Searches 300+ opportunity sources
- 💻 Modern web interface
- 🚀 Railway/Render/Heroku deployment ready
- 📱 Custom email input functionality
- 🔄 Refresh opportunities on demand

🚀 Ready for deployment to Railway, Render, or Heroku!"
else
    echo "✅ Repository already has commits"
fi

echo ""
echo "🎉 GitHub setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Create a repository on GitHub"
echo "2. Add remote origin:"
echo "   git remote add origin https://github.com/akshaymittal143/eb1a-opportunity-finder.git"
echo "3. Push to GitHub:"
echo "   git push -u origin main"
echo "4. Deploy to Railway/Render/Heroku using the repository"
echo ""
echo "📚 Documentation:"
echo "- README.md - Complete setup guide"
echo "- DEPLOYMENT_GUIDE.md - Deployment instructions" 
echo "- RAILWAY_DEPLOYMENT.md - Railway troubleshooting"
echo ""
echo "⚠️  IMPORTANT:"
echo "- Edit .env with your Gmail App Password"
echo "- Never commit .env to GitHub (it's in .gitignore)"
echo "- Enable 2FA on Gmail before generating App Password"
echo ""
echo "🚀 Ready to deploy your EB-1A Opportunity System!" 