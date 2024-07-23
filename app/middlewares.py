from traceback import print_exception

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from models import ExceptionHandlerModel

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> ExceptionHandlerModel:
        """
        Process internal server errors and return in the response.

        :return: ExceptionHandlerModel
        """
        try:
            return await call_next(request)
        except Exception as e:
            print_exception(e)
            return JSONResponse(
                status_code=500, 
                content={
                    'error': e.__class__.__name__, 
                    'messages': e.args
                })