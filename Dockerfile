FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create cache directory
RUN mkdir -p cache

# Expose port
EXPOSE 5003

# Set environment variables
ENV FLASK_APP=src.main
ENV FLASK_ENV=production
ENV PORT=5003

# Run the application
CMD ["gunicorn", "src.main:app", "--bind", "0.0.0.0:5003", "--workers", "4"] 