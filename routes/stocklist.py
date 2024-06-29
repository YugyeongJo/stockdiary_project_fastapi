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

# stocklist
@router.get("/", response_class=HTMLResponse) 
async def stocklist_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist.html", context={'request':request})

@router.post("/", response_class=HTMLResponse) 
async def stocklist_function(
    request:Request
    ,page_number: Optional[int] = 1
    ):

    # DB 불러오기 / 페이지네이션
    conditions = {}
    
    stock_lists, pagination = await collection_stocklist.getsbyconditionswithpagination(
    conditions, page_number
    )

    return templates.TemplateResponse(
        name="stocklist/stocklist.html"
        , context={'request':request,'stock_lists':stock_lists, 'pagination':pagination})

#### -------------------------------------------------------------------------------------------------------

# stocklist_write
@router.get("/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_write.html", context={'request':request})

@router.post("/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(
    request:Request
    ):

    # 작성부분
    form_data = await request.form()
    dict_form_data = dict(form_data)

    stock_list = stocklist(**dict_form_data)
    await collection_stocklist.save(stock_list)

    return templates.TemplateResponse(name="stocklist/stocklist_write.html", context={'request':request})

#### -------------------------------------------------------------------------------------------------------

# stocklist_read
@router.get("/stocklist_read", response_class=HTMLResponse) 
async def stocklist_read_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_read.html", context={'request':request})

@router.post("/stocklist_read", response_class=HTMLResponse) 
async def stocklist_read_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_read.html", context={'request':request})