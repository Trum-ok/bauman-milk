from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import coins_router
# from .routes.players import router as players_router
# from .routes.squads import router as squads_router

app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "https://192.168.55.93",
    "https://192.168.55.93:8000",
    "https://192.168.55.93:443" 
    # если фронтенд на другом порту
    # другие разрешенные источники
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(players_router)
app.include_router(coins_router)
# app.include_router(squads_router)

@app.get("/")
async def root():
    return {"message": "ok"}

# if __name__ == "__main__":
    # 
