# 베이스 이미지 설정
FROM python:3.11

WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 컨테이너 실행 명령어
CMD ["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]