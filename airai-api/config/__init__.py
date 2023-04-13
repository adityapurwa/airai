import os

from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


class FastAPISettings():
    cors_allow_origins = os.getenv("CORS_ALLOW_ORIGINS", "*")
    cors_allow_credentials = os.getenv("CORS_ALLOW_CREDENTIALS", "true") == "true"
    cors_allow_methods = os.getenv("CORS_ALLOW_METHODS", "*")
    cors_allow_headers = os.getenv("CORS_ALLOW_HEADERS", "*")

    def apply(self, app):
        app.add_middleware(CORSMiddleware,
                           allow_origins=self.cors_allow_origins,
                           allow_credentials=self.cors_allow_credentials,
                           allow_methods=self.cors_allow_methods,
                           allow_headers=self.cors_allow_headers)

        app.state.limiter = limiter
        app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
