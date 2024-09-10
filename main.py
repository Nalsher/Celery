import ssl

from fastapi import FastAPI, Request
from endpoints.users_crud import router
from endpoints.table import table_router, create_table
from endpoints.mailverification import mail


app = FastAPI()

app.include_router(mail)
app.include_router(router)
app.include_router(table_router)

@app.middleware("http")
async def chechk_ip(request:Request,call_next):
    user = request.client.host
    response = await call_next(request)
    print(user,'IP HEREEEEEEEEEEEEEEEEEEEEEEEEE')
    return response