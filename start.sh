#!/bin/bash

# Railway Start Script for EB-1A Opportunity System

echo "🚀 Starting EB-1A Opportunity System on Railway..."

# Create necessary directories
mkdir -p cache
mkdir -p src/database

# Set up database (create tables if they don't exist)
echo "🗄️ Setting up database..."
python -c "
import sys
sys.path.insert(0, '.')
try:
    from src.main import app, db
    with app.app_context():
        db.create_all()
    print('✅ Database setup complete')
except Exception as e:
    print(f'⚠️ Database setup warning: {e}')
"

# Start the application with gunicorn
echo "🔥 Starting web server..."
exec gunicorn src.main:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile - 