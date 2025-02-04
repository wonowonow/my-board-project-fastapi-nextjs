from Backend.dto.PostCreateDto import PostCreateDto
from Backend.dto.PostDto import PostDto
from Backend.Model.Post import Post
from Backend.repository.PostRespository import save_post, fetch_posts
from sqlalchemy.orm import Session
from datetime import datetime

def create_post(request: PostCreateDto, db: Session):
    """
    Post 를 생성하는 로직입니다.
    """

    post = Post(
        title=request.title,
        content=request.content,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    return save_post(post, db)

def get_posts(db: Session):
    """
    Post 리스트를 반환하는 로직입니다.
    """

    return fetch_posts(db)