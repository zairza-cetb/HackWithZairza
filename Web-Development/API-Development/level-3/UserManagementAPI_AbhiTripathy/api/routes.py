from fastapi import APIRouter, HTTPException
from models.models import User, user_list
from uuid import UUID

router = APIRouter()


@router.get("/api/user")
def get_users():
    return {"users": user_list}


@router.post("/api/user")
def create_user(user: User):
    user_list.append(user)
    return {"status": "Successfully Added", "User": user}


@router.get("/api/user/{id}")
def get_user(id: UUID):
    for user in user_list:
        if user.id == id:
            return {"User": user}
    raise HTTPException(
        status_code=404, detail="Users not found for this id.")


@router.put("/api/user/{id}")
def update_user(id: UUID, new_user: User):
    if id != new_user.id:
        raise HTTPException(status_code=400, detail="Path ID does not match user ID in request body.")
    for i, user in enumerate(user_list):
        if user.id == new_user.id:
            user_list[i] = new_user
            return {"Update": "Successful", "user after update": user_list[i]}
    raise HTTPException(
        status_code=404, detail="Users not found for this id.")


@router.delete("/api/user/{id}")
def delete_user(id: UUID):
    for i, user in enumerate(user_list):
        if user.id == id:
            del user_list[i]
            return {"Delete": "Successful"}
    raise HTTPException(
        status_code=404, detail="Users not found for this id.")
