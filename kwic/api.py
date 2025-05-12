from fastapi import FastAPI
from typing import List
from .pipeline import Pipeline

app = FastAPI()
pipeline = Pipeline("pipeline.yml")

@app.post("/kwic")
def kwic_endpoint(lines: List[str]):
    results = pipeline.run(lines)
    return {"results": results}