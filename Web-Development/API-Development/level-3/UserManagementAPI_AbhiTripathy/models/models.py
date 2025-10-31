from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr
    name: str
    age: int


user_list = [
    User(email="alice@example.com", name="Alice Smith", age=30),
    User(email="bob.j@example.com", name="Bob Johnson", age=25),
    User(email="charlie.g@example.com", name="Charlie Garcia", age=42),
    User(email="diana.lee@example.com", name="Diana Lee", age=28),
    User(email="evan.p@example.com", name="Evan Patel", age=35),
    User(email="fiona.m@example.com", name="Fiona Miller", age=51),
    User(email="george.k@example.com", name="George Kim", age=19),
    User(email="hannah.w@example.com", name="Hannah Wright", age=65),
    User(email="ian.d@example.com", name="Ian Davis", age=31),
    User(email="julia.r@example.com", name="Julia Rodriguez", age=22),
    User(email="kevin.b@example.com", name="Kevin Brown", age=45),
    User(email="laura.c@example.com", name="Laura Chen", age=29),
    User(email="mike.t@example.com", name="Mike Taylor", age=38),
    User(email="nina.h@example.com", name="Nina Hernandez", age=47),
    User(email="oliver.s@example.com", name="Oliver Scott", age=24),
    User(email="paula.w@example.com", name="Paula Wilson", age=33),
    User(email="quinn.e@example.com", name="Quinn Evans", age=50),
    User(email="ryan.m@example.com", name="Ryan Moore", age=27),
    User(email="sara.j@example.com", name="Sara Jackson", age=36),
    User(email="tom.a@example.com", name="Tom Allen", age=40),
]
