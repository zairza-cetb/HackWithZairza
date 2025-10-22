# Pandarudra — Quotes API

Small Express API that serves a collection of quotes. It's intentionally tiny so you can run and test it quickly.

## Summary

- Language: JavaScript (ES Modules)
- Framework: Express
- Base route: `/api`
- Purpose: expose quote data (all quotes, random quote, quotes by category, categories list)

## Run the server

1. Install dependencies

```batch
cd pandarudra
npm install
```

2. Start server

```batch
npm run start    # production: node index.js
npm run dev      # development with nodemon (if installed)
```

By default the server listens on the port set in `PORT` env var or `3000`.

## Endpoints

All endpoints are prefixed with `/api` (see `index.js`).

1. GET /api/quotes

- Description: Returns an array of all quote texts (strings).
- Response: 200 OK
- Example response:

```json
["The only way to do great work is to love what you do.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "Don't let yesterday take up too much of today.", ...]
```

2. GET /api/quotes/random

- Description: Returns a single random quote's text (string).
- Response: 200 OK
- Example response:

```json
"The only way to do great work is to love what you do."
```

3. GET /api/quotes/category/:category

- Description: Returns an array of full quote objects (id, text, author, category) for the given category.
- Path param: `:category` (e.g. `motivation`, `success`, `life`)
- Response: 200 OK
- Example response:

```json
[
  {
    "id": 1,
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs",
    "category": "motivation"
  },
  {
    "id": 4,
    "text": "The secret of getting ahead is getting started.",
    "author": "Mark Twain",
    "category": "motivation"
  }
]
```

4. GET /api/categories

- Description: Returns a list of unique categories available in the dataset.
- Response: 200 OK
- Example response:

```json
[
  "motivation",
  "success",
  "life",
  "perseverance",
  "wisdom",
  "leadership",
  "growth",
  "creativity",
  "innovation"
]
```

## Quick curl examples (try locally)

```batch
curl -s http://localhost:3000/api/quotes
curl -s http://localhost:3000/api/quotes/random
curl -s http://localhost:3000/api/quotes/category/motivation
curl -s http://localhost:3000/api/categories
```

Note: on Windows `curl` is available in recent versions. You can also use Postman or the included `test/api.rest` file to exercise the endpoints.

## Data

The quotes array is defined in `data/mockdata.js`. Each quote object contains:

- id: number
- text: string
- author: string
- category: string

## Files of interest

- `index.js` — app bootstrap and middleware
- `routes/quote.routes.js` — route definitions
- `controllers/quote.controller.js` — handlers and response shapes
- `data/mockdata.js` — sample quotes dataset
- `test/api.rest` — simple requests you can import into REST clients

## Notes and next steps

- This API is read-only and uses in-memory data. To persist data, add a database and update controllers.
- Consider adding schema validation (e.g., with Joi) and tests for the endpoints.

Enjoy! If you'd like, I can add a short Postman collection or expand the README with examples for integrating the API into a front-end.
