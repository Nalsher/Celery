from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from users.crud import users_add,users_get
from db.dbengine import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from users.crud import users_add


router = APIRouter(
    prefix="/user"
)

class Base(BaseModel):
    pass

class Model(Base):
    name: str
    login: str
    password: str
    info: str
    email: str

class List(Model):
    list: list[Model]


@router.post("/")
async def create_user(model:Model,session:AsyncSession = Depends(get_session)):
    user = await users_add(session,model)
    try:
        await session.commit()
    except:
        raise HTTPException("Err,status_code(422)")
@router.get("/")
async def listen_users(session:AsyncSession = Depends(get_session)):
    user = await users_get(session)
