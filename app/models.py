from __future__ import annotations

from typing import List, Optional
from uuid import UUID

from pydantic import (
    BaseModel
)

class SuccessResponse(BaseModel):
    success: Optional[bool] = None
    response: Optional[str| dict| list] = None
    requestId: Optional[UUID] = None

class ExceptionHandlerModel(BaseModel):
    error: Optional[str] = None
    messages: Optional[str| dict| list] = None

