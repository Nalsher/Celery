from fastapi import APIRouter,Header,Depends
from users.jt.tokens import emailjwt_read
from users.users import users_check
from db.dbengine import get_session
from sqlalchemy.ext.asyncio import AsyncSession



mail = APIRouter(prefix='/email')


@mail.get("/{uuid}")
async def verification(uuid,session:AsyncSession = Depends(get_session)):
    print('IIIIIIIIIIIIIIIIIIIIIIIIIIIII\n',uuid,'\nHHHHHHHHHHHHHHHHHHHHHHHHHH')
    id = await emailjwt_read(uuid)
    aboba = await users_check(session,id)
    if type(aboba) == str:
        return aboba
    else:
        return 'Your account is now active'






