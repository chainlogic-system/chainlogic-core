from fastapi import FastAPI
from visibility.learning_visibility_engine import LearningVisibilityEngine

app = FastAPI(title="ChainLogic API")

engine = LearningVisibilityEngine()


# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "ChainLogic Level 150"
    }


# =========================
# SNAPSHOT (CORE VISIBILITY OUTPUT)
# =========================
@app.get("/snapshot")
def snapshot():
    result = engine.build_snapshot(
        brain_score=0.78,
        risk=0.52,
        evolution={"best": "S0"},
        world_score=0.61,
        mutation_rate=0.29
    )

    return {
        "status": "success",
        "snapshot": result
    }
