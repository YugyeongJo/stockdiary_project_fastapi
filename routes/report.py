from database.connection import Database
from fastapi import APIRouter, Request, FastAPI
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from beanie import PydanticObjectId
from typing import Optional
from datetime import datetime

app = FastAPI()
router = APIRouter()

# db 연결
from models.stocklist import stocklist
collection_stocklist = Database(stocklist)

templates = Jinja2Templates(directory="templates/")

#### -------------------------------------------------------------------------------------------------------

# report
@router.get("/", response_class=HTMLResponse) 
async def report_function(request:Request):
        # DB 불러오기 / 페이지네이션
    
    stock_lists = await collection_stocklist.get_all()
    return templates.TemplateResponse(name="report.html", context={'request':request})

@router.post("/", response_class=HTMLResponse) 
async def report_function(request:Request):
    return templates.TemplateResponse(name="report.html", context={'request':request})