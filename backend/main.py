from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routes import router
import os

app = FastAPI(
    title="Agriculture Support Triage Agent",
    description="Reactive triage agent for Agriculture communications using LLM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

# Serve static files (CSS, JS) from the frontend directory
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    # Serve index.html directly for the root path
    index_path = os.path.join("frontend", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Agriculture Triage Agent API is running"}
