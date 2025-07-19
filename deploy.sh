#!/bin/bash

# EB-1A Opportunity System Deployment Script

echo "🚀 Deploying EB-1A Opportunity System..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your configuration:"
    echo ""
    echo "EMAIL_USERNAME=your-email@gmail.com"
    echo "EMAIL_PASSWORD=your-app-password"
    echo "SMTP_SERVER=smtp.gmail.com"
    echo "SMTP_PORT=587"
    echo "PORT=5003"
    echo ""
    exit 1
fi

# Load environment variables
source .env

# Check required environment variables
if [ -z "$EMAIL_USERNAME" ] || [ -z "$EMAIL_PASSWORD" ]; then
    echo "❌ Error: EMAIL_USERNAME and EMAIL_PASSWORD must be set in .env file"
    exit 1
fi

echo "✅ Environment variables loaded"

# Create necessary directories
mkdir -p cache
mkdir -p src/database

echo "✅ Directories created"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Dependencies installed"

# Run database migrations (if any)
echo "🗄️ Setting up database..."
python -c "from src.main import app, db; app.app_context().push(); db.create_all()"

echo "✅ Database setup complete"

# Start the application
echo "🚀 Starting EB-1A Opportunity System..."
echo "📍 Web interface: http://localhost:5003"
echo "📍 API status: http://localhost:5003/api/system/status"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python src/main.py 