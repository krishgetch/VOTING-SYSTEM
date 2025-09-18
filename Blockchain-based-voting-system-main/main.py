from fastapi import FastAPI
from routes import router
import uvicorn

app = FastAPI(title="Blockchain-Based Voting API")

# Include API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
