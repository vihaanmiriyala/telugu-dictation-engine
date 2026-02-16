# Telugu Dictation Engine - Week 1

## Goal
Working end-to-end skeleton for Telugu dictation.

## Repo Structure
- `frontend/`: Web-first UI. Handles browser microphone access and audio recording.
- `backend/`: FastAPI server. Receives audio, logs telemetry, and returns stub responses.
- `infra/`: Placeholder for Docker and deployment configurations.
- `eval/`: Scripts for evaluating Telugu transcription accuracy (WER).
- `data/`: Storage for sample audio clips and ground truth text.
- `docs/`: Project documentation and architecture blueprints.

## Deliverables Status
- [x] Record audio in browser
- [x] Send to backend
- [x] Stub transcription response (Telugu)
- [x] Logging & basic telemetry (latency, audio duration)
- [ ] Architecture doc (Planned for later)
