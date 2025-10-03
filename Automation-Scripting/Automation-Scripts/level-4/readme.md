# Level 4: Scheduled Automation with Notifications

Build production-ready automation scripts with scheduling, comprehensive logging, error handling, and notification systems. Implement robust workflows that run unattended.

## Project Options

### Option 1: Automated Backup System
Schedule backups with compression, rotation, and status notifications.

**Features:**
- Schedule daily/weekly backups
- Compress files/folders
- Maintain backup rotation (keep last N backups)
- Upload to cloud storage (optional)
- Email/Slack notifications on success/failure
- Detailed logging

### Option 2: System Monitoring and Alerting
Monitor system resources and send alerts on thresholds.

**Features:**
- Monitor CPU, memory, disk usage
- Check service health
- Log metrics over time
- Alert on threshold violations
- Generate daily summary reports
- Configurable via YAML/JSON

### Option 3: Automated Report Generator
Generate and distribute reports on schedule.

**Features:**
- Fetch data from multiple sources
- Generate PDF/Excel reports
- Apply templates and styling
- Email reports to recipients
- Archive previous reports
- Error recovery and retry logic

## Implementation Example
```
import schedule
import time
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import json

Setup logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
logging.FileHandler('automation.log'),
logging.StreamHandler()
]
)

def send_notification(subject, message, config):
"""Send email notification."""
try:
msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = config['from_email']
msg['To'] = config['to_email']

text
    with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
        server.starttls()
        server.login(config['smtp_user'], config['smtp_password'])
        server.send_message(msg)
    
    logging.info(f"Notification sent: {subject}")
except Exception as e:
    logging.error(f"Failed to send notification: {e}")
def backup_task(config):
"""Perform backup task."""
try:
logging.info("Starting backup task...")

text
    # Backup logic here
    # ...
    
    logging.info("Backup completed successfully")
    send_notification(
        "Backup Successful",
        f"Backup completed at {datetime.now()}",
        config
    )
    
except Exception as e:
    logging.error(f"Backup failed: {e}")
    send_notification(
        "Backup Failed",
        f"Error: {e}",
        config
    )
def load_config(config_file):
"""Load configuration from JSON file."""
with open(config_file, 'r') as f:
return json.load(f)

def main():
# Load configuration
config = load_config('config.json')

text
# Schedule tasks
schedule.every().day.at(config['backup_time']).do(backup_task, config)

logging.info("Scheduler started")

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
if name == "main":
main()
```

## Configuration Example

**config.json:**
```
{
"backup_time": "02:00",
"backup_path": "/data",
"backup_destination": "/backups",
"retention_days": 7,
"smtp_server": "smtp.gmail.com",
"smtp_port": 587,
"smtp_user": "your_email@gmail.com",
"smtp_password": "your_password",
"from_email": "your_email@gmail.com",
"to_email": "admin@example.com"
}
```

## Technical Requirements

1. **Scheduling system** (schedule library or cron)
2. **Comprehensive logging** with rotation
3. **Error handling and recovery**
4. **Notification system** (email/Slack/webhook)
5. **Configuration file** for settings
6. **Graceful shutdown** handling
7. **Status monitoring and health checks**

## Dependencies

```
schedule>=1.2.0
python-dotenv>=1.0.0
requests>=2.31.0
pyyaml>=6.0
```

## Submission Requirements

Folder: `AutomationTool_YourGitHubUsername/` containing:

1. `main.py` - Main automation script
2. `config.json.example` - Configuration template
3. `requirements.txt` - Dependencies
4. `README.md` - Setup and deployment guide
5. `systemd/` - Service files (optional)
6. `tests/` - Unit tests

## Deployment Guide

**Running as systemd service:**
```
[Unit]
Description=Automation Script
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/script
ExecStart=/usr/bin/python3 main.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## Resources

- [Python schedule Library](https://schedule.readthedocs.io/)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [Python smtplib](https://docs.python.org/3/library/smtplib.html)
- [Cron Tutorial](https://crontab.guru/)
