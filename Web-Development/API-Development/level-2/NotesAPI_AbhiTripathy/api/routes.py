from fastapi import APIRouter, HTTPException
from models.models import notes_list, Note
from uuid import UUID

router = APIRouter()


@router.get("/api/notes")
def get_notes():
    return {"Notes": notes_list}


@router.post("/api/notes")
def create_note(note: Note):
    notes_list.append(note)
    return {"status": "Successfully Added", "note": note}


@router.get("/api/notes/{id}")
def get_note(id: UUID):
    for note in notes_list:
        if note.id == id:
            return {"Note": note}
    raise HTTPException(
        status_code=404, detail="Notes not found for this id.")


@router.put("/api/notes/{id}")
def update_note(new_note: Note):
    for i, note in enumerate(notes_list):
        if note.id == new_note.id:
            notes_list[i] = new_note
            return {"Update": "Successful", "Note after update": notes_list[i]}
    raise HTTPException(
        status_code=404, detail="Notes not found for this id.")


@router.delete("/api/notes/{id}")
def delete_note(id: UUID):
    for i, note in enumerate(notes_list):
        if note.id == id:
            del notes_list[i]
            return {"Delete": "Successful"}
    raise HTTPException(
        status_code=404, detail="Notes not found for this id.")
