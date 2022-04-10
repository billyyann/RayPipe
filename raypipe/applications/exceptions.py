from typing import Optional
from fastapi import FastAPI, Request, Response,status
from fastapi.responses import ORJSONResponse
from pydantic.main import BaseModel


class RayPipeError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class APIErrorResponse(BaseModel):
    error: Optional[str] = None

def handle_raypipe_error(request: Request, exc: RayPipeError) -> ORJSONResponse:
    err_res = APIErrorResponse(error=str(exc))
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content=err_res.dict()
    )


_EXCEPTION_HANDLERS = {RayPipeError: handle_raypipe_error}