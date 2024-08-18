from fastapi import FastAPI
from app.api.endpoints import books, students, inventory
from app.db import models
from app.db.session import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(books.router, prefix="/api")
app.include_router(students.router, prefix="/api")
app.include_router(inventory.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Library Management System"}
