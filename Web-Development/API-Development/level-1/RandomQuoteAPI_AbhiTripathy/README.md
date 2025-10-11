# RandomQuoteAPI_AbhiTripathy

Lightweight FastAPI project that serves a small collection of mock quotes. Useful as a Level-1 mock data REST API for learning routing, status codes, and JSON responses.

## Setup instructions

Prerequisites:
- Python 3.11+ installed
- pip (or pip3)(if uv is not installed)

1. Install uv (if you don't have it):
```powershell
pip install uv
```

2. Install dependencies (from pyproject.toml):
Do this from the root directory(directory where pyproject.toml lives)
```powershell
uv sync
```

3. Run the app locally (from the project root where `app.py` lives):
```powershell
uv run uvicorn app:app --reload --port 8000
```
The API will be served at http://127.0.0.1:8000. Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

## Available endpoints

All endpoints return JSON. Successful responses use HTTP 200. If a category is invalid the request will return an error (validator raises 400).

- GET /api/quotes
  - Description: Return all quotes (list of quote objects)

- GET /api/quotes/random
  - Description: Return a single random quote

- GET /api/quotes/category/{category}
  - Description: Return all quotes matching the provided category (case-sensitive)
  - Note: The project uses an internal validator to allow only existing categories

- GET /api/categories
  - Description: Return the set of available categories

Additionally, a simple health-check is available:

- GET /
  - Description: Returns a textual health-check JSON

## Data model
Each quote object has the following shape:
```
{
  "id": int,
  "text": string,
  "author": string,
  "category": string
}
```
The project contains 25 mock quotes in `models/models.py`.

## Example requests and responses
1) Get all quotes

Request:
GET http://127.0.0.1:8000/api/quotes

Response (200):
```json
{
  "Quotes": [
    {
      "id": 1,
      "text": "The only way to do great work is to love what you do.",
      "author": "Steve Jobs",
      "category": "Inspiration"
    },
    // ... more quotes ...
  ]
}
```

2) Get a random quote

Request:
GET http://127.0.0.1:8000/api/quotes/random

Response (200):
```json
{
  "Quote": {
    "id": 7,
    "text": "So we beat on, boats against the current, borne back ceaselessly into the past.",
    "author": "F. Scott Fitzgerald",
    "category": "Literature"
  }
}
```

3) Get quotes by category

Request:
GET http://127.0.0.1:8000/api/quotes/category/Wisdom

Response (200):
```json
{
  "Category": "Wisdom",
  "Quotes": [
    {
      "id": 2,
      "text": "The only true wisdom is in knowing you know nothing.",
      "author": "Socrates",
      "category": "Wisdom"
    },
    {
      "id": 17,
      "text": "It is the mark of an educated mind to be able to entertain a thought without accepting it.",
      "author": "Aristotle",
      "category": "Wisdom"
    }
  ]
}
```

If an invalid category is passed the validator will reject it and FastAPI will return a 422 Unprocessable Entity (validation error). To list valid categories use `/api/categories`.

4) Get available categories

Request:
GET http://127.0.0.1:8000/api/categories

Response (200):
```json
{
  "Categories": [
    "Inspiration",
    "Wisdom",
    "Humor",
    "Love",
    "Science",
    "Art",
    "Literature",
    "History",
    "Technology",
    "Philosophy",
    "Success",
    "Life",
    "Courage",
    "Friendship",
    "Nature"
  ]
}
```

## Technology used
- Python 3.11+
- FastAPI - lightweight ASGI framework
- Uvicorn - ASGI server for development
- Pydantic - data validation and models

## Project structure
```
RandomQuoteAPI_AbhiTripathy/
├── app.py
├── api/
│   ├── routes.py
│   ├── __init__.py
├── models/
│   ├── models.py
│   └── __init__.py
├── README.md
├── pyproject.toml
├── .python-version
├── .gitignore
```
