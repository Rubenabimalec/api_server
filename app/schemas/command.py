from pydantic import BaseModel
from typing import List

class CommandRequest(BaseModel):
    command: str
    params: List[str] = []