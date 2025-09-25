from fastapi import FastAPI

app = FastAPI (
    title="Beverage Recommendation API"
)

@app.get("/health", tags=["status"])
def health() -> dict:
    return {"status": "ok"}

