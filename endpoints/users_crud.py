from fastapi import APIRouter, HTTPException, Depends, Header, Cookie, Response
from pydantic import BaseModel
from users.crud import users_add,users_get
from db.dbengine import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from users.crud import users_add
from users.jt.tokens import jwt_check
from users.users import user_get, user_give_jwt


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


@router.post("/")
async def create_user(model:Model,session:AsyncSession = Depends(get_session)):
    user = await users_add(session,model)
    try:
        await session.commit()
    except:
        raise HTTPException("Err,status_code(422)")


@router.post("/auth")
async def authenticate(response: Response,model:Auth,session:AsyncSession = Depends(get_session)):
    try:
        jwt = await user_give_jwt(login=model.login,password=model.password,session=session)
        response.set_cookie(key="jwt",value=str(jwt))
        return {"Success":"Your jwt token now in your cookie-storage"}
    except:
        return {"Error":"Invalid login or password"}



@router.get("/{login}")
async def listen_users(session:AsyncSession = Depends(get_session),key:str = Header(),login:str | None = None):
    try:
        check = await jwt_check(token=key)
        if check == True:           # Esli jwt ne ustarel
            info = await user_get(session,login)
            return {"Information":info}
        else:
            return {"Error": "User may not exist,or your key expired"}
    except:
        return {"Error":"User may not exist,or your key expired"}