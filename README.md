# telugu-dictation-engine

This project follows a modular structure to ensure that the UI, the AI model, and the testing logic can evolve independently.

1. frontend/ (The Interface)
What it does: This folder contains the web-based UI.

Logic: It captures audio from the user’s microphone using the browser's MediaRecorder API and sends the audio data (Blobs) to the backend.

Key Files: index.html (The UI and transcription display).



3. backend/ (The Engine)
What it does: The Python-based server that handles the "heavy lifting."

Logic: It receives audio files, stores them temporarily, calculates processing telemetry (latency/duration), and generates the transcription.

Current State: It uses a "stub" (placeholder) for Telugu text to verify the end-to-end connection.



5. infra/ (The Foundation)
What it does: Contains configuration for deployment.

Logic: This is where Dockerfiles or cloud deployment scripts live, ensuring the app runs exactly the same on a server as it does on your laptop.



7. eval/ (The Grader)
What it does: Accuracy and performance testing.

Logic: Contains scripts to calculate WER (Word Error Rate). Since Telugu is a morphologically rich language, this folder is critical for measuring how well the AI is actually performing.



9. data/ (The Library)

What it does: Storage for testing assets.

Logic: Holds sample Telugu audio clips and "ground truth" (correct) text files. This allows us to run the eval scripts against known data.



10. docs/ (The Blueprint)
What it does: Technical documentation.

Logic: Holds the Architecture Document, design decisions, and future roadmap.
