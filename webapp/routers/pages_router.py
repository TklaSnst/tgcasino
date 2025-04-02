from pathlib import Path
from database import Motor
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response


router = APIRouter(
    prefix="/page",
    tags=["pages"]
)

templates_path = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory="webapp/templates")
user_collection = Motor(collection="user")

@router.get("/main/")
async def main_page(request: Request, response: Response):
    v = {}
    # user = await user_collection.get_user(tg_id=request.)
    v['request'] = request
    v['balance'] = 100
    v['username'] = "pampersss"
    return templates.TemplateResponse('main.html', v)


# @router.post("/game/")
# async def game_start(bet: int, ):
