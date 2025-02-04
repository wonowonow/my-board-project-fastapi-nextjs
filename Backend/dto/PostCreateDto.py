from pydantic import BaseModel

class PostCreateDto(BaseModel):
    title: str
    content: str