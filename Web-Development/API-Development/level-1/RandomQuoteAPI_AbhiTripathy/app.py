from fastapi import FastAPI
from api import routes
    
app = FastAPI()

@app.get("/")
def health_check():
    return {"Health Check": "Successful"}

app.include_router(routes.router)