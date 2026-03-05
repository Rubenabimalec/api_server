from fastapi import FastAPI
from routes.system import router as system_router

app = FastAPI(title="Linux Command Executor API")

app.include_router(system_router)