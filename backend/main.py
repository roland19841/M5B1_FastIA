from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger

from modules.calcul import calcul

app = FastAPI(title="FastIA API Template")

class CalculRequest(BaseModel):
    value: int = Field(..., description="Entier à mettre au carré")

class CalculResponse(BaseModel):
    result: int

@app.get("/")
def root():
    logger.info("GET /")
    return {"message": "FastIA API template is running"}

@app.get("/health")
def health():
    logger.info("GET /health")
    return {"status": "ok"}

@app.post("/calcul", response_model=CalculResponse)
def do_calcul(payload: CalculRequest):
    logger.info(f"POST /calcul value={payload.value}")
    res = calcul(payload.value)
    return {"result": res}
