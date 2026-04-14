from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from config import settings




app = FastAPI()

print("settings\n\n\n" , settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}


@app.get("/ping")
def ping():
    res = {
        "data" : "PONG",
        "message" : "system is able to communicate"
    }
    return JSONResponse(content=res, status_code=200)





if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )