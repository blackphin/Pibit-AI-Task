# FastAPI Imports
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# SlowAPI Rate Limiter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

# Routers Import
from routers import routers

# ENV Variables
from config import settings


# FastAPI app Init
app = FastAPI(
    title="Pibit AI",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


# Middleware

# CORS
origins = ["*"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTPS Redirect
# app.add_middleware(HTTPSRedirectMiddleware)


# Rate Limiter
limiter = Limiter(key_func=get_remote_address,
                  default_limits=[settings.rate_limit])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Routers
app.include_router(routers.router)


# Backend Healthcheck Route
@app.get("/api/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Backend Server Active"}
