from pathlib import Path

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response


router = APIRouter(
    prefix="/page",
    tags=["pages"]
)

templates_path = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory="templates")


@router.get("/main/")
async def main_page(request: Request, response: Response):
    return templates.TemplateResponse('main.html', {"request": request})