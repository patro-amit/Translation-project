# LinguaLink - Deployment & Configuration Guide

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd "Translation project"

# Create virtual environment
python3 -m venv venv310
source venv310/bin/activate  # On Windows: venv310\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
nano .env
```

### 3. Download Model Weights

Download `pytorch_model.bin` from Google Drive and place in:
```
models/facebook/nllb-200-distilled-600M/pytorch_model.bin
```

Or use gdown:
```bash
pip install gdown
gdown --id 1gYF0sLhNv7_9P4hpzPPli0tANkmmQl9I -O models/facebook/nllb-200-distilled-600M/pytorch_model.bin
```

### 4. Run the Application

#### Development Mode:
```bash
python app.py
```

#### Production Mode:
```bash
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

---

## Environment Variables

### Required:
- `SECRET_KEY`: Flask secret key for sessions (auto-generated if not set)

### Optional:
- `FLASK_ENV`: `development` or `production` (default: development)
- `FLASK_DEBUG`: `True` or `False` (default: True)
- `FLASK_HOST`: Server host (default: 0.0.0.0)
- `FLASK_PORT`: Server port (default: 5001)

---

## Production Deployment

### Using Gunicorn + Nginx

#### 1. Install Production Server:
```bash
pip install gunicorn
```

#### 2. Create Gunicorn Config:
```python
# gunicorn_config.py
bind = "0.0.0.0:5001"
workers = 4
worker_class = "sync"
timeout = 120
keepalive = 5
errorlog = "logs/gunicorn_error.log"
accesslog = "logs/gunicorn_access.log"
loglevel = "info"
```

#### 3. Run with Gunicorn:
```bash
gunicorn -c gunicorn_config.py app:app
```

#### 4. Nginx Configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    client_max_body_size 16M;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 120s;
    }

    location /static {
        alias /path/to/Translation project/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

### Using Systemd Service

Create `/etc/systemd/system/lingualink.service`:
```ini
[Unit]
Description=LinguaLink Translation Service
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/path/to/Translation project
Environment="PATH=/path/to/Translation project/venv310/bin"
ExecStart=/path/to/Translation project/venv310/bin/gunicorn -c gunicorn_config.py app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable lingualink
sudo systemctl start lingualink
sudo systemctl status lingualink
```

---

## Docker Deployment

### Dockerfile:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create necessary directories
RUN mkdir -p uploads instance logs

# Expose port
EXPOSE 5001

# Run application
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
```

### Docker Compose:
```yaml
version: '3.8'

services:
  lingualink:
    build: .
    ports:
      - "5001:5001"
    volumes:
      - ./models:/app/models
      - ./uploads:/app/uploads
      - ./instance:/app/instance
      - ./logs:/app/logs
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - FLASK_ENV=production
      - FLASK_DEBUG=False
    restart: unless-stopped
```

Build and run:
```bash
docker-compose up -d
```

---

## Security Checklist

### Before Production:

- [ ] Set strong `SECRET_KEY` in environment
- [ ] Disable debug mode (`FLASK_DEBUG=False`)
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure CORS properly
- [ ] Set up rate limiting
- [ ] Enable security headers
- [ ] Configure firewall rules
- [ ] Set up backup strategy
- [ ] Enable monitoring and logging
- [ ] Review file upload permissions
- [ ] Implement user authentication (if needed)
- [ ] Add CAPTCHA for public access

---

## Performance Optimization

### 1. Model Loading:
```python
# Pre-load models at startup
with app.app_context():
    utils.initialize_models()
```

### 2. Caching:
```bash
# Install Redis
pip install flask-caching redis

# Configure in app.py
from flask_caching import Cache
cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
})
```

### 3. Database Optimization:
```python
# Add indexes
db.create_all()
db.session.execute('CREATE INDEX idx_timestamp ON translation_log(timestamp DESC)')
```

---

## Monitoring

### Application Logging:
```python
# Configure in app.py
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

### Health Check Endpoint:
```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}
```

---

## Backup Strategy

### Database Backup:
```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)
cp instance/translations.db backups/translations_$DATE.db
find backups/ -name "translations_*.db" -mtime +7 -delete
```

### Automated Backups:
```cron
# Run daily at 2 AM
0 2 * * * /path/to/backup.sh
```

---

## Troubleshooting

### Issue: Models not loading
**Solution:** Ensure `pytorch_model.bin` is downloaded and path is correct

### Issue: Out of memory
**Solution:** Reduce worker count or use smaller Whisper model (tiny/base)

### Issue: Slow translation
**Solution:** 
- Use GPU if available
- Increase worker count
- Implement caching for common translations

### Issue: Upload failures
**Solution:** Check `uploads/` directory permissions and MAX_CONTENT_LENGTH

---

## Maintenance

### Update Dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Clear Old Uploads:
```bash
find uploads/ -type f -mtime +1 -delete
```

### Database Vacuum:
```bash
sqlite3 instance/translations.db "VACUUM;"
```

---

## Support & Documentation

- **Application Report:** See `APPLICATION_ANALYSIS_REPORT.md`
- **Fixed Issues:** See `FIXES_SUMMARY.md`
- **API Documentation:** Coming soon
- **User Guide:** Coming soon

---

## License & Credits

- **Framework:** Flask
- **Translation Model:** Meta NLLB-200
- **OCR:** EasyOCR
- **STT:** OpenAI Whisper
- **TTS:** Google TTS

---

**Version:** 2.0  
**Last Updated:** February 9, 2026  
**Status:** ✅ Production Ready
