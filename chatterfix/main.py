import os
import time
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import openai

from chatterfix.routes import ai, workorders, assets, pm, technicians, parts, review_routes, assist

# Initialize FastAPI app
app = FastAPI(title="ChatterFix CMMS")

# ---- Logging Setup ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger("chatterfix")

# ---- CORS Setup ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Global Health Tracking ----
start_time = time.time()
error_counter = 0

# ---- Setup OpenAI ----
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Missing OpenAI API Key. Set OPENAI_API_KEY in environment variables.")

# ---- Mount Frontend Static Files ----
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/out"))
if os.path.exists(frontend_path):
    app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")
    logger.info(f"Serving frontend static files from {frontend_path}")
else:
    logger.warning(f"Frontend build folder not found at {frontend_path}")

# ---- API Routers ----
app.include_router(ai.router, prefix="/ai")
app.include_router(workorders.router, prefix="/workorders")
app.include_router(assets.router, prefix="/assets")
app.include_router(pm.router, prefix="/pm")
app.include_router(technicians.router, prefix="/technicians")
app.include_router(parts.router, prefix="/parts")
app.include_router(review_routes.router, prefix="/review")
app.include_router(assist.router, prefix="/assist")

# ---- Middleware: Request Logger ----
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Completed response: {request.method} {request.url.path} - {response.status_code}")
    return response

# ---- Exception Handler: AI Error Summarizer ----
@app.exception_handler(Exception)
async def ai_exception_handler(request: Request, exc: Exception):
    global error_counter
    error_counter += 1
    try:
        from chatterfix.services.openai_chat import run_chat
        error_summary = await run_chat(f"Summarize this Python error and suggest a fix:\n{str(exc)}")
    except Exception as e:
        error_summary = f"Error summarization unavailable. (Reason: {e})"

    logger.error(f"Unhandled Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": str(exc), "ai_summary": error_summary}
    )

# ---- Health Check Endpoints ----
@app.get("/health")
async def health_check():
    uptime = int(time.time() - start_time)
    return {
        "status": "healthy",
        "uptime_seconds": uptime,
        "errors_detected": error_counter,
    }

@app.get("/ai/heal")
async def ai_heal():
    uptime = int(time.time() - start_time)
    return {
        "message": "AI Diagnostics Complete.",
        "uptime_seconds": uptime,
        "errors_detected": error_counter,
        "suggestion": "Monitor error patterns. Restart services if persistent errors occur."
    }

# ---- Root Welcome Route ----
@app.get("/")
async def root():
    return {"message": "Welcome to ChatterFix CMMS API"}