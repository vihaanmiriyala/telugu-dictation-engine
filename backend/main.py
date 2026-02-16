import time
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # Added this

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- NEW: Serve the Frontend UI ---
@app.get("/")
async def read_index():
    # This looks for your index.html in the frontend folder
    return FileResponse("../frontend/index.html")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    start_process = time.perf_counter()
    content = await file.read()
    file_size = len(content)
    
    duration_sec = round(file_size / 32000, 2)
    stub_text = "నమస్కారం, ఇది ఒక నమూనా ప్రతిలేఖనం."
    
    time.sleep(0.5)
    latency_ms = round((time.perf_counter() - start_process) * 1000, 2)
    
    return {
        "transcript": stub_text,
        "telemetry": {
            "latency": f"{latency_ms}ms",
            "duration": f"{duration_sec}s"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
