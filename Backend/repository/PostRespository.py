from sqlalchemy.orm import Session
from Backend.Model import Post

def save_post(post: Post, db: Session) -> Post:
    db.add(post)  # DB에 추가
    db.commit()  # 트랜잭션 적용
    db.refresh(post)  # 저장된 데이터 새로고침

    # 엔티티 반환
    return post