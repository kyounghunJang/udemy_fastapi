from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from starlette import status    
import models
from database import engine, SessionLocal
from routers import auth
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)