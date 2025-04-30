
from fastapi import Body, FastAPI
from.import models
from .database import engine,get_db
from app.routers import user,post,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
import os
print(f"Starting FastAPI on port {os.getenv('PORT', 10000)}")
#models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)
app.include_router(vote.router)
print(settings.database_username)
@app.get("/")
def root():
    return {"message": "welcome to api!!"}



