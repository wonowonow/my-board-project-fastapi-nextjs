from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Backend.Service import PostService
from Backend.dto.PostCreateDto import PostCreateDto
from Backend.dto.PostDto import PostDto
from Backend.database.database import get_db
from typing import List

router = APIRouter()

@router.post("/posts", response_model=PostDto)
def create_post(request: PostCreateDto, db: Session = Depends(get_db)):
    return PostService.create_post(request, db)

@router.get("/posts", response_model=List[PostDto])
def get_posts(db: Session = Depends(get_db)):
    return PostService.get_posts(db)

@router.get("/posts/{post_id}", response_model=PostDto)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return PostService.get_post(post_id, db)