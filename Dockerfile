# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for OpenCV, EasyOCR, and Whisper
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Hugging Face Spaces requires running as a non-root user
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Update ownership and copy the rest of the application files
WORKDIR $HOME/app
COPY --chown=user . $HOME/app

# Hugging Face Spaces routes web traffic to port 7860 by default
EXPOSE 7860

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Command to run the application using Flask's built-in server on port 7860
CMD ["flask", "run", "--host=0.0.0.0", "--port=7860"]
