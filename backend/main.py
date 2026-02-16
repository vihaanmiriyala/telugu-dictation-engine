import time
import os
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Start telemetry timer
    start_process = time.perf_counter()
    
    # Simulate receiving the audio file
    content = await file.read()
    file_size = len(content)
    
    # Calculate basic telemetry: Audio Duration (Estimate)
    # Most browser recordings are ~32KB per second
    duration_sec = round(file_size / 32000, 2)
    
    # STUB TRANSCRIPTION (Fake)
    # "నమస్కారం, ఇది ఒక నమూనా ప్రతిలేఖనం." (Hello, this is a sample transcription.)
    stub_text = "నమస్కారం, ఇది ఒక నమూనా ప్రతిలేఖనం."
    
    # Simulate a small "processing" delay
    time.sleep(0.5)
    
    # Calculate telemetry: Latency
    latency_ms = round((time.perf_counter() - start_process) * 1000, 2)
    
    # LOGGING (Deliverable: Basic telemetry events)
    print(f"--- Telemetry Event ---")
    print(f"File Received: {file.filename}")
    print(f"Audio Duration: {duration_sec}s")
    print(f"Processing Latency: {latency_ms}ms")
    print(f"-----------------------")

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
