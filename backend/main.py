from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.lecture import router as lecture_router
from routers.live import router as live_router
from routers.email import router as email_router

app = FastAPI(
    title="ClassNote AI Backend",
    description="AI-powered lecture transcription and translation backend",
    version="1.0.0"
)

# Secure yet flexible CORS for local development environments
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://127.0.0.1:8080",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lecture_router)
app.include_router(live_router)
app.include_router(email_router)


@app.get("/")
async def home():
    return {
        "project": "ClassNote AI",
        "status": "online",
        "message": "ClassNote AI Backend is running successfully!"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "backend": "FastAPI",
        "project": "ClassNote AI"
    }
