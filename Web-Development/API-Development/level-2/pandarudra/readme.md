# Notes API — pandarudra

This is a small Notes CRUD API used for learning Express and building REST endpoints. This README documents all available endpoints, example requests/responses, seeded data, and how to test them locally.

## Base URL

- Local (default): http://localhost:3000
- API prefix used in this project: `/api` (so full base for endpoints below is `http://localhost:3000/api`)

## Seeded data

The project ships with a few seeded notes in `db/notes.js`. Example seeded IDs you can use in requests:

- `f96070ed-1141-4266-accc-339790b540be` — Welcome Note
- `e83579d0-7983-4886-9d78-3de1355d5670` — Todo List
- `86ce0bb7-745f-4703-ac2a-9eb6f2178171` — REST Client created note
- `4105f430-0777-4167-96ff-bbdc08564bd6` — REST Client created note

> Note: If the project writes back to `db/notes.js` during runtime (create/update/delete), those seeded IDs may change depending on implementation. Use the seeded IDs above for testing GET endpoints.

## Endpoints

All endpoints are under `/api/notes`.

1. Get all notes

- Method: GET
- Path: `/api/notes`
- Description: Returns an array of all notes.
- Response (200):

```json
[
  {
    "id": "f96070ed-1141-4266-accc-339790b540be",
    "title": "Welcome Note",
    "content": "This is your first note in the Notes API!",
    "tags": ["welcome","intro"],
    "createdAt": "2025-10-07T08:37:12.675Z",
    "updatedAt": "2025-10-07T08:37:12.676Z"
  },
  ...
]
```

2. Get single note by id

- Method: GET
- Path: `/api/notes/:id`
- Description: Returns a single note matching the given `:id`.
- Success (200): returns the note object.
- Not found (404): returns a message indicating the note wasn't found.

Example request (curl):

```bash
curl -i http://localhost:3000/api/notes/f96070ed-1141-4266-accc-339790b540be
```

3. Create a new note

- Method: POST
- Path: `/api/notes/`
- Content-Type: application/json
- Body (JSON):

```json
{
  "title": "REST Client created note",
  "content": "Use this note to test update & delete.",
  "tags": ["rest", "test"]
}
```

- Success (201): returns the newly created note object including a generated `id`, `createdAt`, and `updatedAt` fields.
- Validation error (400): returned when required fields are missing or invalid.

Example (curl):

```bash
curl -i -X POST http://localhost:3000/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title":"REST Client created note","content":"Use this note to test update & delete.","tags":["rest","test"]}'
```

4. Update an existing note

- Method: PUT
- Path: `/api/notes/:id`
- Content-Type: application/json
- Body: Same shape as create (title, content, tags). The server should update `updatedAt` automatically.
- Success (200): returns the updated note object.
- Not found (404): when `:id` does not exist.

Example (curl):

```bash
curl -i -X PUT http://localhost:3000/api/notes/f96070ed-1141-4266-accc-339790b540be \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated title (REST)","content":"Updated content (REST)","tags":["updated","rest"]}'
```

5. Delete a note

- Method: DELETE
- Path: `/api/notes/:id`
- Success (200 or 204): note is removed and an appropriate confirmation is returned.
- Not found (404): when `:id` does not exist.

Example (curl):

```bash
curl -i -X DELETE http://localhost:3000/api/notes/f96070ed-1141-4266-accc-339790b540be
```

## Testing locally (VS Code REST Client or curl)

- VS Code REST Client: Use the `test/api.rest` file in this repo. Open it and click "Send Request" for each request.
- curl (Windows CMD):

```powershell
# Get all notes
curl -i http://localhost:3000/api/notes

# Create a note
curl -i -X POST http://localhost:3000/api/notes/ -H "Content-Type: application/json" -d "{\"title\":\"REST Client created note\",\"content\":\"Use this note to test update & delete.\",\"tags\":[\"rest\",\"test\"]}"
```

> Tip: After creating a note, copy the `id` value from the JSON response and use it for PUT/GET/DELETE calls.

## Troubleshooting

- If you see an error like "The requested module '../db/notes.js' does not provide an export named 'notes'":

  - Ensure `db/notes.js` exports `notes` as an ESM export (`export const notes = [...]`).
  - Alternatively, require the file using CommonJS (`const { notes } = require('../db/notes.js')`) depending on your project module type. This project uses ESM imports in controllers.

- If UUID generation is needed in runtime (for newly created notes) prefer Node's built-in `crypto.randomUUID()` (Node v14.17+). Example in code:

```js
import { randomUUID } from "crypto";
const id = randomUUID();
```

## Quick start (run the server)

1. Install dependencies:

```powershell
npm install
```

2. Start in dev mode (if script present):

```powershell
npm run dev
```

or start normally:

```powershell
npm start
```

3. Open `test/api.rest` in VS Code or use curl as shown above.

## File references

- Routes: `pandarudra/routes/note.routes.js`
- Controllers: `pandarudra/controllers/note.controller.js`
- Seed DB: `pandarudra/db/notes.js`
- Tests (REST client): `pandarudra/test/api.rest`

---

If you want, I can also: validate and patch `db/notes.js` to export the `notes` array, add UUID generation in the controller when creating notes, and run a quick smoke test. Tell me which of those you'd like done next.
