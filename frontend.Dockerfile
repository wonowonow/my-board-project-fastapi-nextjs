# Node.js 베이스 이미지
FROM node:18

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 파일 복사 후 종속성 설치
COPY Frontend/package.json Frontend/package-lock.json ./
RUN npm install

# 소스 코드 복사
COPY Frontend /app

# Next.js 빌드
RUN npm run build

# Next.js 실행
CMD ["npm", "run", "start"]