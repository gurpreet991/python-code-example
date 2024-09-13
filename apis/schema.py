from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class EmailSchema(BaseModel):
    subject: Optional[str] = Field(None, description="Subject of the email.")
    recipients: List[str] = Field(
        None, description="List of email user.")
    stream: str
