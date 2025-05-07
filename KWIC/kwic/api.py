from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from kwic.algorithms import circular_shifts, kwic_key

app = FastAPI()

class KWICRequest(BaseModel):
    lines: List[str]

class KWICResponse(BaseModel):
    result: List[str]

@app.post("/kwic", response_model=KWICResponse)
def kwic_endpoint(req: KWICRequest) -> KWICResponse:
    result: List[str] = []
    for line in req.lines:
        result.extend(circular_shifts(line))
    result.sort(key=kwic_key)
    return KWICResponse(result=result)