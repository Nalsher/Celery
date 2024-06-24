from fastapi import APIRouter, HTTPException, Depends
from db.dbtables import drop_table,create_table


table_router = APIRouter(
    prefix="/table"
)

@table_router.get("/delete")
async def delete():
    await drop_table()
    return {"Deleting":"done"}

@table_router.get("/create")
async def create():
    await create_table()
    return {"Creating":"done"}