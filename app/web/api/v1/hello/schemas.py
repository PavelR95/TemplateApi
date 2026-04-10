# Base
# Requirements
from pydantic import BaseModel


class BaseMessage(BaseModel):
    message: str = "Hello, World!"
