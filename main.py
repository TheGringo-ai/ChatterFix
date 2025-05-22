import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# This commit is from TheGringo-ai

# Load environment variables
load_dotenv()

# App and logging setup
app = FastAPI()
logging.basicConfig(level=logging.INFO)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Try importing routes and fail gracefully
try:
    from routes import (
        ai_console,
        workorders,
        assets,
        parts,
        schedule,
        technician_logs,
        debug_routes
    )

    app.include_router(ai_console.router)
    app.include_router(workorders.router)
    app.include_router(assets.router)
    app.include_router(parts.router)
    app.include_router(schedule.router)
    app.include_router(technician_logs.router)
    app.include_router(debug_routes.router)
except Exception as e:
    logging.exception("Failed to import or register routes")

@app.get("/")
def home():
    return {"message": "ChatterFix FastAPI is live"}
