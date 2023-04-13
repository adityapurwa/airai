# AirAI
AirAI is a website that helps people search for the current air quality situation in their area. It is built using the Vite JavaScript framework.

# Requirements
Node.js 18.0 or higher

# Installation
To install AirAI, clone the repository and navigate to the project directory:

```sh
git clone https://github.com/adityapurwa/airai.git
cd airai/airai-web
```
Then, install the project dependencies using npm:

```sh
npm install
```

# Configuration

Before running AirAI, you need to set up the following environment variables:

- VITE_API_BASE_URL - The base URL of the AirAI API, including the port number (e.g. http://localhost:8000)
- VITE_STATIC_MAP_KEY - Your API key for the Google Maps Static API

> VITE_STATIC_MAP_KEY is optional. If you do not set this variable, the map will not be displayed.
 
You can create a .env file in the project root directory and set these variables there:

```dotenv
VITE_API_BASE_URL=http://localhost:8000
VITE_STATIC_MAP_KEY=your-api-key
```
Note: Do not commit the .env file to version control.

# Usage
To run AirAI in development mode, use the following command:

```sh
npm run dev
```

To build the production version of the website, use the following command:

```sh
npm run build
```

This will generate a dist directory containing the optimized build. You can then serve this directory using a static file server of your choice.

# License
The AirAI source code is GNU AGPLv3 licensed.