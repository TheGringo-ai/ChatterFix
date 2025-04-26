from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from App.routes import workorders, assets, pm, ai, technicians, parts
from App.routes.assist import router as assist_router

app = FastAPI(title="ChatterFix CMMS")

# ✅ Allow frontend from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Core CMMS modules
app.include_router(workorders.router, prefix="/workorders")
app.include_router(assets.router, prefix="/assets")
app.include_router(pm.router, prefix="/pm")
app.include_router(ai.router, prefix="/ai")
app.include_router(technicians.router)
app.include_router(parts.router)

# ✅ AI Assistant helper routes
app.include_router(assist_router)

# ✅ Health & Root
@app.get("/")
def root():
    return {"message": "Welcome to ChatterFix CMMS API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}