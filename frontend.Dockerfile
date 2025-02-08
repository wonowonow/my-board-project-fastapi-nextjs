# 기존 Node.js 이미지 사용
FROM node:20 

# 작업 디렉토리 설정
WORKDIR /app

# pnpm 설치 (추가)
RUN npm install -g pnpm

# 패키지 복사 및 설치
COPY Frontend/package.json Frontend/package-lock.json ./
RUN npm install

# 불필요한 node_modules 삭제
RUN rm -rf node_modules

# 프로젝트 코드 복사
COPY Frontend/ .

# 빌드 실행
RUN npm run build

CMD ["npm", "run", "start"]