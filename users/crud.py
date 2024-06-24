import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from db.dbtables import users
from users.jt.tokens import jwt_create, emailjwt_create
from sqlalchemy import select
from CeleryTask.taska import send_message


async def users_add(sesion:AsyncSession,model:dict):
    async with sesion as sess:
        new_user = users(name=model.name,login=model.login,email=model.email,
                         password=model.password,info=model.info,uuid=uuid.uuid4())
        new_user.token = await jwt_create(new_user)
        await send_message(new_user)
        sess.add(new_user)
        await sess.commit()
        return new_user

async def users_get(session:AsyncSession):
    async with session as sess:
        us = select(users)
        res = await sess.execute(us)
        for user_obj in res.scalars():
            print("Obj-name - " + user_obj.name + "\nObj-Token - " + user_obj.token + "\nObj-UUID - ",user_obj.uuid)
