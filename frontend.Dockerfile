# Node.js 베이스 이미지
FROM node:20

# 작업 디렉토리 설정
WORKDIR /app

# package.json & package-lock.json 복사
COPY package.json package-lock.json ./

# 패키지 설치
RUN npm install

# 소스 코드 복사
COPY . .

# Next.js 빌드
RUN npm run build

# Next.js 실행
CMD ["npm", "run", "start"]