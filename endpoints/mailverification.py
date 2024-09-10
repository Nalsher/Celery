from fastapi import APIRouter,Header,Depends
from users.jt.tokens import emailjwt_read
from users.UserService import UserService
from users.Dependencies import User_Service_Return
from db.dbengine import get_session
from sqlalchemy.ext.asyncio import AsyncSession



mail = APIRouter(prefix='/email')


@mail.get("/{uuid}")
async def verification(uuid,session:AsyncSession = Depends(get_session),
                       Service:UserService = Depends(User_Service_Return)):
    very = await Service.user_check(session=session,id=uuid)







