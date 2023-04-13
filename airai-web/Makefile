install:
	npm install

build:
	npm run build

preview:
	npm run preview

build-docker:
	docker build -t airai-web:latest .

run-docker:
	docker run --rm -d -p 41730:4173 --env-file .env --name airai-web airai-web:latest