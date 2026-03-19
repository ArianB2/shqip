from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes import health, lessons, vocabulary

app = FastAPI(
    title="Shqip API",
    description="Albanian language learning app — Gheg & Tosk dialects",
    version="0.1.0",
)

# CORS — allows the React frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, tags=["health"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
app.include_router(vocabulary.router, prefix="/vocabulary", tags=["vocabulary"])


@app.get("/")
def root():
    return {
        "app": "Shqip",
        "description": "Albanian language learning API",
        "docs": "/docs",
    }
