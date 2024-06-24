import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from db.dbtables import users
from users.jt.tokens import jwt_create, emailjwt_create
from sqlalchemy import select


async def users_mail_veryf(session:AsyncSession,model:users):
    async with session as sess:
        query = select(users.is_active).where(users.uuid==model.uuid)
        result = sess.execute(query)
        user = result.scalar_one()
        user.is_active = True
        sess.add(user)
        await sess.commit()

async def users_check(session:AsyncSession,id:dict):
    async with session as sess:
        query = select(users).where(users.is_active == False, users.uuid == id.get('uuid'))
        result = await sess.execute(query)
        try:
            final = result.scalar_one()
            final.is_active = True
            sess.add(final)
            await sess.commit()
            return final
        except:
            return 'This account already verificated or not exist'


