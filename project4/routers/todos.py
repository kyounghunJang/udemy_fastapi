from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app =FastAPI()
models