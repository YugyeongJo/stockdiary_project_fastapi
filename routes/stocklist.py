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

@router.post("/", response_class=HTMLResponse) 
async def stocklist_function(
    request:Request
    ,page_number: Optional[int] = 1
    ):
    
    form_data = await request.form()
    dict_form_data = dict(form_data)
    btn_type = dict_form_data['btn_type']
    dict_id = dict_form_data['id']
    dict_form_data.pop('btn_type')
    dict_form_data.pop('id')
    stock_list = stocklist(**dict_form_data)
    
    # 작성부분
    if btn_type == 'write':
        await collection_stocklist.save(stock_list)
    
    elif btn_type == 'update':
        await collection_stocklist.update_one(dict_id,dict_form_data)
        
    elif btn_type == 'delete':
        await collection_stocklist.delete_one(dict_id)
    

    # DB 불러오기 / 페이지네이션
    conditions = {}
    
    stock_lists, pagination = await collection_stocklist.getsbyconditionswithpagination(
    conditions, page_number
    )
    
    # 삭제하기
    
    

    return templates.TemplateResponse(
        name="stocklist/stocklist.html"
        , context={'request':request,'stock_lists':stock_lists, 'pagination':pagination})

#### -------------------------------------------------------------------------------------------------------

# stocklist_write
@router.get("/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_write.html", context={'request':request})

@router.post("/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_write.html", context={'request':request})

#### -------------------------------------------------------------------------------------------------------

# stocklist_read
@router.get("/stocklist_read/{object_id}", response_class=HTMLResponse) 
async def stocklist_read_function(
    request:Request
    , object_id:PydanticObjectId
    ):

    stock_lists = await collection_stocklist.get(object_id)

    return templates.TemplateResponse(
        name="stocklist/stocklist_read.html"
        , context={'request':request,'stock_list':stock_lists})

@router.post("/stocklist_read", response_class=HTMLResponse) 
async def stocklist_read_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_read.html", context={'request':request})