from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class RouteModel(BaseModel):
    id: Optional[int] = None
    path: str = Field(..., min_length=1)
    method: HttpMethod
    description: str
    requiresAuth: bool = False
    permissions: str = "public"
    requiredFields: List[str] = []
    api: Optional[str] = None
    lastModifiedBranch: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
