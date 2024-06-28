from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class stocklist(Document):
    user_ID: Optional[str] = None
    
  
    class Settings:
        name = "stocklist"