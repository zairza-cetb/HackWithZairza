# Level 3: Web Scraping Tools

Build web scraping tools to extract data from websites ethically. Implement rate limiting, respect robots.txt, and handle various website structures.

## Project Options

### Option 1: News Article Scraper
Extract articles from news websites with metadata.

**Features:**
- Extract title, author, date, content
- Handle pagination
- Save to CSV or JSON
- Download images (optional)
- Respect rate limits

### Option 2: Product Price Tracker
Monitor product prices across e-commerce sites.

**Features:**
- Track multiple products
- Store price history
- Detect price changes
- Generate price trends
- Send alerts on price drops

### Option 3: Job Listing Aggregator
Collect job postings from multiple job boards.

**Features:**
- Search by keywords and location
- Extract job details (title, company, salary, description)
- Remove duplicates
- Export to structured format
- Schedule daily updates

## Implementation Example
```
import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

def scrape_articles(url, max_pages=5):
"""Scrape articles from a news website."""
articles = []

for page in range(1, max_pages + 1):
    print(f"Scraping page {page}...")
    
    try:
        # Request page
        response = requests.get(f"{url}?page={page}", 
                                headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract articles
        for article in soup.find_all('article', class_='post'):
            title = article.find('h2').text.strip()
            link = article.find('a')['href']
            date = article.find('time')['datetime']
            
            articles.append({
                'title': title,
                'link': urljoin(url, link),
                'date': date
            })
        
        # Rate limiting
        time.sleep(2)
        
    except Exception as e:
        print(f"Error on page {page}: {e}")
        continue

return articles


def save_to_csv(articles, filename):
"""Save articles to CSV file."""
with open(filename, 'w', newline='', encoding='utf-8') as f:
writer = csv.DictWriter(f, fieldnames=['title', 'link', 'date'])
writer.writeheader()
writer.writerows(articles)

print(f"Saved {len(articles)} articles to {filename}")

if name == "main":
    url = "https://example-news-site.com"
    articles = scrape_articles(url, max_pages=3)
    save_to_csv(articles, "articles.csv")
```


## Technical Requirements

1. **Respect robots.txt**
2. **Implement rate limiting** (2-3 seconds between requests)
3. **Handle errors gracefully**
4. **Use appropriate User-Agent**
5. **Parse HTML correctly**
6. **Export structured data**

## Ethical Guidelines

- Check robots.txt before scraping
- Implement delays between requests
- Don't overload servers
- Respect terms of service
- Only scrape public data
- Add contact information in User-Agent

## Dependencies
```
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
```


## Submission Requirements

Folder: `Scraper_YourGitHubUsername/` containing:

1. `scraper.py` - Main scraping script
2. `requirements.txt` - Dependencies
3. `README.md` - Usage and ethical guidelines
4. `output/` - Sample output files

## Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://requests.readthedocs.io/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
