# AirAI

> AirAI is a project that aims to provide a chat interface for air quality dashboard.

# Components

This project contains two components

- API `./airai-api`
- Web `./airai-web`

# Development

> The dockerfile is for deployment/preview only.
> For development, please refer to the README.md in each component.
> Running the API and Web locally is preferred for development.

## API

Refer to `./airai-api/README.md`

## Web

Refer to `./airai-web/README.md`

# Running

## Docker

> **Preparing Environment**:
>
> Copy `.api.env.example` to `.api.env` and fill in the values.
>
> Copy `.web.env.example` to `.web.env` and fill in the values.

To run the API and the Web interface, run the following command:

```bash
docker-compose up
```

You should be able to access the web interface at `http://localhost:4173`

## Manually

### API

Open `airai-api` folder and run the following command:

```bash
./venv/bin/pip install -r requirements.txt
./venv/bin/python -m uvicorn main:app
```

### Web

Open `airai-web` folder and run the following command:

```bash
npm install
npm run dev
```

# License

AGPL-3.0