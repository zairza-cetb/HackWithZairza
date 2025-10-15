# BasicCRUDAPI_AbhiTripathy

A small Level-2 FastAPI project implementing CRUD operations for an in-memory Notes resource. The API demonstrates request validation with Pydantic models, UUID-based identifiers, and basic error handling.

## Setup instructions

Prerequisites:
- Python 3.11+ installed
- uv

1. Install uv if you don't have it:
```bash
pip install uv
```
1. (Optional) Create and activate a virtual environment using uv:
Inside your project directory
```bash
uv init --python 3.11
```

2. Install dependencies (from the project root):

```bash
uv add fastapi[all]
```

3. Run the app (from project root where `main.py` lives):

```bash
uv run uvicorn main:app --reload --port 8000
```

4. Open the interactive API docs:

http://127.0.0.1:8000/docs

## Available endpoints

All endpoints return JSON. The API manages an in-memory list of notes using the `Note` Pydantic model (see `models/models.py`).

- GET /api/notes
	- Description: Return all notes (list)

- POST /api/notes
	- Description: Create a new note. The request body must match the `Note` model fields (id is optional — generated if omitted).

- GET /api/notes/{id}
	- Description: Return a single note identified by UUID. Returns 404 if not found.

- PUT /api/notes/{id}
	- Description: Update an existing note. The request must contain a `Note` object with its `id` matching the URL. Returns 404 if the note doesn't exist.

- DELETE /api/notes/{id}
	- Description: Delete a note by UUID. Returns 404 if not found.

## Data model

`Note` has the following fields (defined in `models/models.py`):

```python
class Note(BaseModel):
		id: UUID = Field(default_factory=uuid4)
		label: str = Field(default="all")
		title: str
		content: str
```

Example of a Note JSON:

```json
{
	"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	"label": "work",
	"title": "Q4 Project Kickoff",
	"content": "Finalize the project brief for the Q4 initiative..."
}
```

## Example requests and responses

1) Get all notes

Request:

GET http://127.0.0.1:8000/api/notes

Response (200):

```json
{
	"Notes": [
		{
			"id": "...",
			"label": "work",
			"title": "Q4 Project Kickoff",
			"content": "Finalize the project brief..."
		},
		// ...more notes
	]
}
```

2) Create a new note

Request:

POST http://127.0.0.1:8000/api/notes
Content-Type: application/json

```json
{
	"label": "personal",
	"title": "Buy groceries",
	"content": "Milk, eggs, bread"
}
```

Response (200):

```json
{
	"status": "Successfully Added",
	"note": {
		"id": "generated-uuid",
		"label": "personal",
		"title": "Buy groceries",
		"content": "Milk, eggs, bread"
	}
}
```

3) Get a single note

Request:

GET http://127.0.0.1:8000/api/notes/{id}

Response (200):

```json
{
	"Note": {
		"id": "...",
		"label": "shopping",
		"title": "Grocery Shopping",
		"content": "Milk, bread, eggs..."
	}
}
```

If the note is not found the API returns:

Response (404):

```json
{
	"detail": "Notes not found for this id."
}
```

4) Update a note

Request (PUT):

PUT http://127.0.0.1:8000/api/notes/{id}
Content-Type: application/json

Body (must include the same id):

```json
{
	"id": "...",
	"label": "work",
	"title": "Updated Title",
	"content": "Updated content"
}
```

Response (200):

```json
{
	"Update": "Successful",
	"Note after update": {
		"id": "...",
		"label": "work",
		"title": "Updated Title",
		"content": "Updated content"
	}
}
```

5) Delete a note

Request:

DELETE http://127.0.0.1:8000/api/notes/{id}

Response (200):

```json
{
	"Delete": "Successful"
}
```

## Technology used

- Python 3.11+
- FastAPI — web framework
- Uvicorn — ASGI server
- Pydantic — data validation and models

## Project structure

```
BasicCRUDAPI_AbhiTripathy/
├── main.py           # app entry point
├── api/
│   └── routes.py    # API routes
├── models/
│   └── models.py    # Pydantic models + in-memory data
├── uv.lock          # To recreate environment
├── .gitignore
├── .python-version  # To recreate environment
├── pyproject.toml   # To recreate environment
└── README.md
```
