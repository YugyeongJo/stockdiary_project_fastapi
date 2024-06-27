from fastapi import FastAPI
app = FastAPI()

from database.connection import Settings
settings = Settings()
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

from routes.stocklist import router as stocklist_router
from routes.report import router as report_router

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
async def root(Request:Request):
    return templates.TemplateResponse("main.html",{'request':Request})


@app.post("/")
async def root(Request:Request):
    return templates.TemplateResponse("main.html",{'request':Request})