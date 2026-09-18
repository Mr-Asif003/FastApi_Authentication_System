from typing import Any, Optional

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    status: str
    code: int
    data: Optional[Any] = None