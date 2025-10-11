from fastapi import APIRouter
from typing import Annotated
from pydantic import AfterValidator
from random import choice
from models.models import quotes

router = APIRouter()

def all_categories():
    categories = set()
    for x in quotes:
        categories.add(x.category)
    return categories
    
def category_validator(category: str) -> str:
    if category.title() in all_categories():
        return category.title()
    raise ValueError

@router.get("/api/quotes")
def get_all_quotes():
    return {"Quotes": quotes}

@router.get("/api/quotes/random")
def get_random_quote():
    random_quote = choice(quotes)
    return {"Quote": random_quote}

@router.get("/api/quotes/category/{category}")
def get_category_quotes(category: Annotated[str, AfterValidator(category_validator)]):
    category_quotes = []
    for x in quotes:
        if x.category==category:
            category_quotes.append(x)
    return {"Category": category, "Quotes": category_quotes}

@router.get("/api/categories")
def get_categories():
    return {"Categories": all_categories()}