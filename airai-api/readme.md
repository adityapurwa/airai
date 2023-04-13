# AirAI API

AirAI API is a fastapi-based backend for AirAI, a GPT-powered website that enables users to ask about current air
quality in their cities. The API uses langchain in the background and connects with Meteo as the air quality provider.
Meteo was chosen because it is free and does not require API keys.

# Requirements

- Python 3.8 or higher
- Virtualenv

## Environment variables

- **REQUIRED** OPENAI_API_KEY - API key for OpenAI API

```sh
cp .env.example .env
```
> This will create a .env file in the project directory. You can then edit the file to add your API key.

# Installation

To install the dependencies of AirAI API, run the following command in the project directory:

```sh
make install
```

> This will create a virtual environment and install the necessary dependencies specified in the requirements.txt file.

# Usage

To run the AirAI API, use the following command:

```sh
make run
```

> By default, the API will be available at http://localhost:8000.

# Development

To run the AirAI API in development mode, use the following command:

```sh
make dev
```

> This will run the API with automatic reloading enabled. Any changes made to the code will be automatically detected
> and
> reloaded.

# Testing

To run the test suite for the AirAI API, use the following command:

```sh
make test
```

> This will run the test suite using pytest. All tests has test_ prefix in their names.

# License

The AirAI API source code is GNU AGPLv3 licensed.
