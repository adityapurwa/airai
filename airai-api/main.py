from dotenv import load_dotenv
from fastapi import FastAPI

from api.v1 import chat
from config import FastAPISettings

load_dotenv()

app = FastAPI()

# This will configure middleware for the app
# - CORS
fastapi_settings = FastAPISettings()
fastapi_settings.apply(app)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
