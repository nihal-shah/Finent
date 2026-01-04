from pydantic import BaseModel
from datetime import datetime
class Fetching(BaseModel):
    stock: str
    start_date: datetime
    end_date: datetime
