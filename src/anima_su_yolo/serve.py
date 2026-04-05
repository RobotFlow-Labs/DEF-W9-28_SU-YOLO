from __future__ import annotations

from datetime import datetime, timezone


def health() -> dict:
    return {
        "status": "ok",
        "module": "su_yolo",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def ready() -> dict:
    # Readiness can be upgraded to check loaded model and weights.
    return {"ready": True, "module": "su_yolo"}


def predict(payload: dict) -> dict:
    # Placeholder API contract until real inference model loading is attached.
    return {
        "ok": True,
        "module": "su_yolo",
        "message": "predict endpoint scaffolded; bind model runtime in CUDA deployment phase",
        "input_keys": sorted(payload.keys()),
        "detections": [],
    }


app = None
try:
    from fastapi import FastAPI

    app = FastAPI(title="anima-su-yolo", version="0.1.0")

    @app.get("/health")
    def health_route() -> dict:
        return health()

    @app.get("/ready")
    def ready_route() -> dict:
        return ready()

    @app.post("/predict")
    def predict_route(payload: dict) -> dict:
        return predict(payload)

except Exception:
    # Keep module importable even if FastAPI is not installed locally.
    app = None
