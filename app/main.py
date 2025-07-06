from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import aggregated, map, top

app = FastAPI(title="PhonePe Insights API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use specific frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(aggregated.router, prefix="/aggregated")
app.include_router(map.router, prefix="/map")
app.include_router(top.router, prefix="/top")

@app.get("/")
def read_root():
    return {"message": "Welcome to PhonePe Insights API"}
