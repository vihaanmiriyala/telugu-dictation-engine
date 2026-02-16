import time
import os
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Telugu Dictation Engine")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe")
async def transcribe_telugu(file: UploadFile = File(...)):
    start_time = time.perf_counter()
    
    # 1. Save the file
    file_id = f"{uuid.uuid4()}.wav"
    file_path = os.path.join(UPLOAD_DIR, file_id)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    # 2. Telemetry Calculation
    file_size_kb = len(content) / 1024
    duration_est = len(content) / 32000  # Rough estimate for web audio
    
    # 3. Simulate processing "vibe"
    time.sleep(0.7) 
    
    # 4. Telugu Stub Response
    stub_transcript = "నమస్కారం, ఇది తెలుగు డిక్టేషన్ ఇంజిన్ నుండి ఒక నమూనా ప్రతిలేఖనం."

    latency_ms = (time.perf_counter() - start_time) * 1000

    return {
        "success": True,
        "transcript": stub_transcript,
        "telemetry": {
            "latency_ms": round(latency_ms, 2),
            "audio_duration_sec": round(duration_est, 2),
            "file_size_kb": round(file_size_kb, 2)
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
