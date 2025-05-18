from fastapi import FastAPI
from routes import workorders

app = FastAPI()

app.include_router(workorders.router)