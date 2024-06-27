import ssl

from fastapi import FastAPI
from endpoints.users_crud import router
from endpoints.table import table_router
from endpoints.mailverification import mail
from db.dbtables import create_table


app = FastAPI()

app.include_router(mail)
app.include_router(router)
app.include_router(table_router)
