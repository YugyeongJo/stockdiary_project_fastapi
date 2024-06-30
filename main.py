from fastapi import FastAPI
app = FastAPI()

from database.connection import Settings
settings = Settings()

@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

from routes.stocklist import router as stocklist_router
from routes.report import router as report_router
from database.connection import Database
from beanie import PydanticObjectId

from models.stocklist import stocklist
collection_stocklist = Database(stocklist)

from fastapi import Request
from fastapi.templating import Jinja2Templates
app.include_router(stocklist_router, prefix="/stocklist")
app.include_router(report_router, prefix="/report")

templates = Jinja2Templates(directory="templates/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles
# url 경로, 자원 물리 경로, 프로그래밍 측면
app.mount("/data/img", StaticFiles(directory="data/img/"), name="static_img")

@app.get("/")
async def root(request: Request):
    try:
        stock_lists = await collection_stocklist.get_all()
        chart_lists = list(stock_lists)

        dict_count = {'국내': 0, '해외': 0}
        dict_amount = {'국내': 0, '해외': 0}
        for i in chart_lists:
            if i.dict()['investment_country'] == '국내':
                dict_count['국내'] += 1
                dict_amount['국내'] += int(i.dict()['unit_price']) * int(i.dict()['stock_count'])
            else:
                dict_count['해외'] += 1
                dict_amount['해외'] += int(i.dict()['unit_price']) * int(i.dict()['stock_count'])

        dict_domestic = {}
        dict_overseas = {}

        for j in chart_lists:
            stock_name = j.dict()['stock_name']
            stock_count = int(j.dict()['stock_count'])
            if j.dict()['investment_country'] == '국내':
                if stock_name in dict_domestic:
                    dict_domestic[stock_name] += stock_count
                else:
                    dict_domestic[stock_name] = stock_count
            else:
                if stock_name in dict_overseas:
                    dict_overseas[stock_name] += stock_count
                else:
                    dict_overseas[stock_name] = stock_count

        top_domestic = sorted(dict_domestic.items(), key=lambda item: item[1], reverse=True)[:5]
        top_overseas = sorted(dict_overseas.items(), key=lambda item: item[1], reverse=True)[:5]

        top_domestic_with_rank = [(idx+1, stock_name, stock_count) for idx, (stock_name, stock_count) in enumerate(top_domestic)]
        top_overseas_with_rank = [(idx+1, stock_name, stock_count) for idx, (stock_name, stock_count) in enumerate(top_overseas)]

        return templates.TemplateResponse("main.html", {
            'request': request,
            'dict_count': dict_count,
            'dict_amount': dict_amount,
            'top_domestic': top_domestic_with_rank,
            'top_overseas': top_overseas_with_rank
        })
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}


@app.post("/")
async def root(request:Request):
    return templates.TemplateResponse("main.html",{'request':request})