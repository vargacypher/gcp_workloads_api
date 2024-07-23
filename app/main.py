from fastapi import FastAPI
from fastapi import FastAPI, status,Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from uuid import uuid4
from models import SuccessResponse
from routes import router
from middlewares import ExceptionHandlerMiddleware



app = FastAPI(
    contact={'email': 'suporte@vargas.com.br'},
    title='Workloads API',
)

app.include_router(
    router,
    prefix="/v1"
)

app.add_middleware(ExceptionHandlerMiddleware)


@app.exception_handler(RequestValidationError)
async def validation_ex_handler(request: Request, exc: RequestValidationError):
    request_id = uuid4()
    errors = exc.errors()

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "success": False,
            "requestId": request_id,
            "detail": errors
        }),
    )

@app.get('/healthcheck', response_model=SuccessResponse)
def get_status() -> SuccessResponse:
    return {"success": True,'response': '', "requestId": uuid4()}


# OpenAPI customizations
def custom_openapi(ignored=None):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        description='''A Workloads Api permite que você faça cargas de dados
de forma segura e confiável, utilizando padrões REST e corpos das mensagens em
formato JSON.
''',
        version='1.0.0',
        title='Workloads Api',
       routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
