from sqlalchemy.ext.asyncio import AsyncSession
from db.dbtables import users
from users.UserRepository import UserRep


class UserService:
    def __init__(self,UserRepository: UserRep):
        self.UserRepository = UserRep

    async def user_add(self,session: AsyncSession,model: dict):
        await self.UserRepository.users_add(session,model)

    async def user_get(self,session: AsyncSession,model: str):
        user = await self.UserRepository.users_get(session=session,model=model)
        return user

    async def user_get_info(self,session: AsyncSession,login: str,token: str):
        usr = await self.UserRepository.user_get_info(session=session,login=login)
        return usr

    async def user_give_jwt(self,session: AsyncSession,login: str ,password: str):
        jwt = await self.UserRepository.user_give_jwt(session=session,login=login,password=password)
        return jwt

    async def user_check(self,session: AsyncSession,id):
        check = self.UserRepository.users_check(session=session,uuid=id)
        return check

    async def user_mail(self,session: AsyncSession,usr: users):
        await self.UserRepository.users_mail_veryf(session=session,model=usr)
