import time
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# Get the absolute path to the directory this file is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    # Robust pathing to find the index.html
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    start_process = time.perf_counter()
    
    # SAVE the file so we can use it for Eval later
    file_path = os.path.join(UPLOAD_DIR, f"{int(time.time())}.wav")
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    file_size = len(content)
    duration_sec = round(file_size / 32000, 2)
    
    # Telugu Stub
    stub_text = "నమస్కారం, ఇది ఒక నమూనా ప్రతిలేఖనం."
    
    time.sleep(0.5) # Simulate vibe-processing
    latency_ms = round((time.perf_counter() - start_process) * 1000, 2)
    
    return {
        "transcript": stub_text,
        "telemetry": {
            "latency": f"{latency_ms}ms",
            "duration": f"{duration_sec}s"
        }
    }
