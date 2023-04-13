FROM node:18-slim AS build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-slim
WORKDIR /app
COPY --from=build /app .

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4173"]
EXPOSE 4173