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
@router.get("/stocklist", response_class=HTMLResponse) 
async def stocklist_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist.html", context={'request':request})

@router.post("/stocklist", response_class=HTMLResponse) 
async def stocklist_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist.html", context={'request':request})

#### -------------------------------------------------------------------------------------------------------

# stocklist_write
@router.get("/stocklist/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_write.html", context={'request':request})

@router.post("/stocklist/stocklist_write", response_class=HTMLResponse) 
async def stocklist_write_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist.stocklist_write", context={'request':request})

#### -------------------------------------------------------------------------------------------------------

# stocklist_read
@router.get("/stocklist/stocklist_read", response_class=HTMLResponse) 
async def stocklist_read_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist_read.html", context={'request':request})

@router.post("/stocklist/stocklist_read", response_class=HTMLResponse) 
async def stocklist_read_function(request:Request):
    return templates.TemplateResponse(name="stocklist/stocklist.stocklist_read", context={'request':request})