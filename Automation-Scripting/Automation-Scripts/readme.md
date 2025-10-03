# Automation Scripts

This folder contains Python scripts for automating repetitive tasks and workflows. Projects are organized by complexity, from basic file operations to advanced scheduled automation with monitoring and notifications.

## Project Levels

### Level 1: File Organization Scripts
Basic scripts for organizing files based on extensions, dates, or custom rules. Focus on file system operations and directory management.

**Skills:** File I/O, os and shutil modules, path manipulation, basic logic

### Level 2: Data Format Converters
Scripts converting between different data formats including CSV, JSON, XML, and Excel. Handle data transformation and validation.

**Skills:** Data parsing, format conversion, pandas library, error handling

### Level 3: Web Scraping Tools
Extract data from websites using BeautifulSoup and requests. Focus on ethical scraping with rate limiting and robots.txt compliance.

**Skills:** HTTP requests, HTML parsing, data extraction, rate limiting, CSV/JSON output

### Level 4: Scheduled Automation with Notifications
Production-ready automation with scheduling, logging, error handling, and notification systems for email, Slack, or other platforms.

**Skills:** Scheduling (cron, schedule library), logging, email/API notifications, error recovery

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Basic Python knowledge
- Command-line familiarity

## Getting Started

1. Choose a level matching your skill
2. Read level-specific requirements
3. Install required dependencies
4. Implement your script
5. Test with sample data
6. Document usage and edge cases
7. Submit with clear instructions

## Testing Scripts
```
# Install dependencies
pip install -r requirements.txt

# Run script
python script_name.py

# Test with sample data
python script_name.py --input sample_data/
```


## Submission Format

Create a file or folder:
- Single file: `ScriptName_YourGitHubUsername.py`
- With dependencies: `ScriptName_YourGitHubUsername/` containing:
  - `main.py` - Main script
  - `requirements.txt` - Dependencies
  - `README.md` - Documentation
  - `sample_data/` - Test data (optional)

## Resources

- [Python os Module](https://docs.python.org/3/library/os.html)
- [Python shutil Module](https://docs.python.org/3/library/shutil.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
