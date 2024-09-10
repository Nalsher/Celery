from fastapi import APIRouter, HTTPException, Depends, Header, Cookie, Response
from pydantic import BaseModel
from db.dbengine import get_session
from users.Dependencies import User_Service_Return
from users.UserService import UserService
from sqlalchemy.ext.asyncio.session import AsyncSession


router = APIRouter(
    prefix="/user"
)

class Base(BaseModel):
    pass

class Auth(Base):
    login: str
    password: str

class Model(Auth):
    name: str
    info: str
    email: str

class List(Model):
    list: list[Model]


@router.post("/",responses={400:{"description":"Bad Request"}})
async def create_user(model:Model,session:AsyncSession = Depends(get_session),
                      Service:UserService = Depends(User_Service_Return)):
    try:
        user_create = Service.user_add(session=session,model=model)
    except:
        return Response("Unprocessable Entity",status_code=422)

@router.post("/auth")
async def authenticate(response: Response,model:Auth,session:AsyncSession = Depends(get_session),
                       Service:UserService = Depends(User_Service_Return)):
    jwt = await Service.user_give_jwt(session=session,login=model.login,password=model.password)
    if not jwt:
        return Response("Unprocessable Entity",status_code=422)



@router.get("/{login}")
async def listen_users(session:AsyncSession = Depends(get_session),key:str = Header(),
                       login:str | None = None,Service:UserService = Depends(User_Service_Return)):
    info = await Service.user_get_info(session=session,login=login,token=key)
    return info