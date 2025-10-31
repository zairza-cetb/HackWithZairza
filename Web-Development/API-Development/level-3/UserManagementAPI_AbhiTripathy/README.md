# UserManagementAPI_AbhiTripathy

A Level-3 FastAPI project that exposes a simple in-memory User management API. It demonstrates Pydantic validation (including email validation), UUID identifiers, and basic CRUD operations.

## Setup instructions

Prerequisites:
- Python 3.11+ installed
- uv (recommended) or pip

1. Install uv if you don't have it:
```powershell
pip install uv
```

2. Install dependencies (from project root):
```powershell
uv sync
```

3. Run the app (from the project root where `main.py` lives):

```powershell
uv run uvicorn main:app --reload --port 8000
```

4. Open the interactive API docs:

http://127.0.0.1:8000/docs

## Available endpoints

- GET /api/user
  - Description: Return all users

- POST /api/user
  - Description: Create a new user. Request body must follow the `User` model (see Data model). `id` is optional and will be generated if omitted.

- GET /api/user/{id}
  - Description: Return a single user by UUID. Returns 404 if not found.

- PUT /api/user/{id}
  - Description: Update an existing user. The request should contain a full `User` object with matching `id`. Returns 404 if not found.

- DELETE /api/user/{id}
  - Description: Delete a user by UUID. Returns 404 if not found.

## Data model

`User` (defined in `models/models.py`) fields:

```python
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr
    name: str
    age: int
```

Example user JSON:

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "email": "alice@example.com",
  "name": "Alice Smith",
  "age": 30
}
```

The project includes a seeded `user_list` of sample users in `models/models.py`.

## Example requests and responses

1) Get all users

Request:

GET http://127.0.0.1:8000/api/user

Response (200):

```json
{
  "users": [
    {
      "id": "...",
      "email": "alice@example.com",
      "name": "Alice Smith",
      "age": 30
    },
    // ...more users
  ]
}
```

2) Create a new user

Request:

POST http://127.0.0.1:8000/api/user
Content-Type: application/json

```json
{
  "email": "new.user@example.com",
  "name": "New User",
  "age": 21
}
```

Response (200):

```json
{
  "status": "Successfully Added",
  "User": {
    "id": "generated-uuid",
    "email": "new.user@example.com",
    "name": "New User",
    "age": 21
  }
}
```

3) Get a single user

Request:

GET http://127.0.0.1:8000/api/user/{id}

Response (200):

```json
{
  "User": {
    "id": "...",
    "email": "bob.j@example.com",
    "name": "Bob Johnson",
    "age": 25
  }
}
```

If not found, response (404):

```json
{
  "detail": "Users not found for this id."
}
```

4) Update a user

Request (PUT):

PUT http://127.0.0.1:8000/api/user/{id}
Content-Type: application/json

Body (must include the same id):

```json
{
  "id": "...",
  "email": "updated@example.com",
  "name": "Updated Name",
  "age": 31
}
```

Response (200):

```json
{
  "Update": "Successful",
  "user after update": {
    "id": "...",
    "email": "updated@example.com",
    "name": "Updated Name",
    "age": 31
  }
}
```

5) Delete a user

Request:

DELETE http://127.0.0.1:8000/api/user/{id}

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
- Pydantic — data validation (EmailStr) and models

## Project structure

```
UserManagementAPI_AbhiTripathy/
├── main.py
├── api/
│   └── routes.py
├── models/
│   └── models.py
├── pyproject.toml
├── .python-version
└── README.md
```
