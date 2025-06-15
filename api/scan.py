from fastapi import FastAPI
from .utils import run_rsi_scan

app = FastAPI()

@app.get("/api/scan")
def scan_handler():
    results = run_rsi_scan()
    return {"status": "ok", "results": results}
