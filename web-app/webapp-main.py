from pathlib import Path
from routers import pages_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan():
    print('wa-start')
    yield
    print('wa-stop')


static_path = Path(__file__).parent / "static"
app = FastAPI()
app.include_router(pages_router)
app.mount("/static", StaticFiles(directory=static_path), name="static")


if __name__ == "__main__":
    uvicorn.run("webapp-main:app", reload=True)
