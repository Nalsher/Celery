import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from db.dbtables import users
from users.jt.tokens import jwt_create, emailjwt_create, emailjwt_read
from sqlalchemy import select
from CeleryTask.taska import send_message
from fastapi.responses import Response
from users.jt.tokens import jwt_check


class UserRep:

    async def users_add(self,sesion: AsyncSession, model: dict):
        async with sesion as sess:
            new_user = users(name=model.name, login=model.login, email=model.email,
                             password=model.password, info=model.info, uuid=uuid.uuid4())
            new_user.token = await jwt_create(new_user)
            await send_message(new_user)
            sess.add(new_user)
            await sess.commit()
            return new_user

    async def users_get(self,session: AsyncSession, model: str):
        async with session as sess:
            us = select(users).where(users.login == model)
            res = await sess.execute(us)
            obj = res.scalars_one()
            return obj

    async def user_get_info(self,session: AsyncSession, login: str,token: str):
        async with session as sess:
            check = await jwt_check(token)
            if check:
                usr = await self.users_get(session,login)
                return Response(content={"Information":usr.info},status_code=200)
            else:
                return Response(content={"Error": "User may not exist,or your key expired"})
    async def user_give_jwt(self,session: AsyncSession, login: str, password: str):
        async with session as sess:
            usr = await self.users_get(session,login)
            if usr.password == password:
                return Response.set_cookie(key="jwt",value=str(usr.token))
            else:
                return None

    async def users_check(session: AsyncSession, uuid):
        async with session as sess:
            id = emailjwt_read(uuid)
            query = select(users).where(users.uuid == id)
            result = await sess.execute(query)
            result = result.scalar_one()
            if result.is_active == False:
                result.is_active = True
                sess.add(result)
                await sess.commit
                return Response(content="Success,your account is now active",status_code=200)
            else:
                return Response(content='This account already verificated or not exist',status_code=400)

    async def users_mail_veryf(session: AsyncSession, model: users):
        async with session as sess:
            query = select(users.is_active).where(users.uuid == model.uuid)
            result = sess.execute(query)
            user = result.scalar_one()
            user.is_active = True
            sess.add(user)
            await sess.commit()