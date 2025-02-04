from fastapi import FastAPI
from Backend.controller import HelloController, PostController

app = FastAPI()

app.include_router(HelloController.router)
app.include_router(PostController.router)