# ✅ Use Python 3.11 (needed for pandas 2.2.3+)
FROM python:3.11-slim

# Install minimal system dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Ensure Flask can import from src/
ENV PYTHONPATH="/app/src"

# Expose Flask port
EXPOSE 8080

# Run the Flask app (can switch to gunicorn later if needed)
CMD ["python", "app.py"]