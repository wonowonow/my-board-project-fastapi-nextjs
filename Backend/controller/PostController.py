from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Backend.Service import PostService
from Backend.dto.PostCreateDto import PostCreateDto
from Backend.dto.PostDto import PostDto
from Backend.database.database import get_db

router = APIRouter()

@router.post("/post", response_model=PostDto)
def create_post(request: PostCreateDto, db: Session = Depends(get_db)):
    return PostService.create_post(request, db)