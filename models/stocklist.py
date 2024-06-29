from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from datetime import datetime

class stocklist(Document):
    date: Optional[datetime] = None
    stock_name: Optional[str] = None
    stock_count: Optional[int] = None
    stock_amount: Optional[int] = None
    commission: Optional[int] = None
    currency_unit: Optional[str] = None
    unit_price: Optional[int] = None
    exchange_rate: Optional[int] = None
    KRW_conversion: Optional[int] = None
    fractional_investment: Optional[str] = None
    automated_investment: Optional[str] = None
    platform: Optional[str] = None
    investment_country: Optional[str] = None
    account_type: Optional[str] = None
    purchasing_status: Optional[str] = None
    selling_status: Optional[str] = None
    
    class Settings:
        name = "stocklist"