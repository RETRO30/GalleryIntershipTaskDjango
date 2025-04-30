FROM node:23-alpine

ARG VITE_API_URL

ENV VITE_API_URL=$VITE_API_URL

WORKDIR /app
COPY . .
RUN npm install && npm run build
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "5173"]
# RUN npm install
# CMD ["npm", "run", "dev"]