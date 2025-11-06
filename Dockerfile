# ✅ Use Python 3.11 (works with pandas 2.2.x etc.)
FROM python:3.11-slim

# Install minimal system dependencies (e.g., for numpy/scikit-learn)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install dependencies first (better layer caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . /app

# Make sure Flask can import from src/
ENV PYTHONPATH="/app/src"

# Expose Flask port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
