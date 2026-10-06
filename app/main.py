from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router


app = FastAPI(
    title="ComicCraft",
    description="AI Comic Story Creator using Gemini and image generation",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(router)


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }