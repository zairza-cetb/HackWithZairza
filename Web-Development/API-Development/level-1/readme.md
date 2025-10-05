# Level 1: Mock Data REST APIs

Build basic REST APIs with hardcoded data to understand HTTP methods, routing, status codes, and JSON responses. Focus on API structure without database complexity.

## Project Options

### Option 1: Random Quotes API
API serving inspirational quotes with category filtering.

**Endpoints:**
- `GET /api/quotes` - Get all quotes
- `GET /api/quotes/random` - Get random quote
- `GET /api/quotes/category/:category` - Get quotes by category
- `GET /api/categories` - List all categories

**Response Example:**
```
{
"id": 1,
"text": "The only way to do great work is to love what you do.",
"author": "Steve Jobs",
"category": "motivation"
}
```


### Option 2: Programming Jokes API
API providing programming-related jokes and puns.

**Endpoints:**
- `GET /api/jokes` - Get all jokes
- `GET /api/jokes/random` - Get random joke
- `GET /api/jokes/:id` - Get specific joke
- `GET /api/jokes/type/:type` - Filter by type (general, programming, dad jokes)

**Response Example:**
```
{
"id": 1,
"setup": "Why do programmers prefer dark mode?",
"punchline": "Because light attracts bugs!",
"type": "programming"
}
```


### Option 3: Tech Facts API
API serving interesting technology and computer science facts.

**Endpoints:**
- `GET /api/facts` - Get all facts
- `GET /api/facts/random` - Random fact
- `GET /api/facts/topic/:topic` - Facts by topic
- `GET /api/facts/count` - Get total count

## Technical Requirements

1. **HTTP Status Codes:**
   - 200: Success
   - 404: Not Found
   - 400: Bad Request
   - 500: Server Error

2. **Response Format:**
   - All responses in JSON
   - Include status and data fields
   - Error messages for failed requests

3. **Project Structure:**
```
project-name/
├── server.js (or app.py)
├── data/
│ └── mockData.js (or data.json)
├── routes/
│ └── apiRoutes.js
├── package.json (or requirements.txt)
└── README.md
```


## Implementation Example (Express.js)
```
const express = require('express');
const app = express();
const PORT = 3000;

// Mock data
const quotes = [
{ id: 1, text: "Quote 1", author: "Author 1", category: "motivation" },
{ id: 2, text: "Quote 2", author: "Author 2", category: "success" }
];

// Routes
app.get('/api/quotes', (req, res) => {
res.json({ status: 'success', data: quotes });
});

app.get('/api/quotes/random', (req, res) => {
const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
res.json({ status: 'success', data: randomQuote });
});

app.get('/api/quotes/:id', (req, res) => {
const quote = quotes.find(q => q.id === parseInt(req.params.id));
if (!quote) {
return res.status(404).json({ status: 'error', message: 'Quote not found' });
}
res.json({ status: 'success', data: quote });
});

app.listen(PORT, () => console.log("Server running on port ${PORT}"));
```


## Submission Requirements

Include in `APIName_YourGitHubUsername/`:

1. Complete source code
2. At least 20 data items in mock data
3. Minimum 4 endpoints
4. README.md with:
   - Setup instructions
   - Available endpoints
   - Example requests and responses
   - Technology used

## Learning Resources

- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [REST API Tutorial](https://restfulapi.net/)
- [Express.js Routing](https://expressjs.com/en/guide/routing.html)
- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

## Evaluation Criteria

- Code organization
- Endpoint functionality
- Proper HTTP status codes
- JSON response format
- Error handling
- Documentation quality
