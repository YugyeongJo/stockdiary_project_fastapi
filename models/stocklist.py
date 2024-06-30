from typing import Optional, List, Union

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from datetime import datetime

class stocklist(Document):
    date: Optional[datetime] = None
    stock_name: Optional[Union[str, int, float, bool]] = None
    stock_count: Optional[Union[str, int, float, bool]] = None
    stock_amount: Optional[Union[str, int, float, bool]] = None
    commission: Optional[Union[str, int, float, bool]] = None
    currency_unit: Optional[str] = None
    unit_price: Optional[Union[str, int, float, bool]] = None
    exchange_rate: Optional[Union[str, int, float, bool]] = None
    KRW_conversion: Optional[Union[str, int, float, bool]] = None
    fractional_investment: Optional[str] = None
    automated_investment: Optional[str] = None
    platform: Optional[str] = None
    investment_country: Optional[str] = None
    account_type: Optional[str] = None
    purchasing_status: Optional[str] = None
    selling_status: Optional[str] = None
    stock_memo: Optional[str] = None
    
    class Settings:
        name = "stocklist"