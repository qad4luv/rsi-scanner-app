from fastapi import FastAPI
from utils import get_rsi  # ✅ Absolute import

app = FastAPI()

@app.get("/api/scan")
def scan_handler():
    results = run_rsi_scan()
    return {"status": "ok", "results": results}
