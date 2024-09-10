from users.UserRepository import UserRep
from users.UserService import UserService


UserRepo = UserRep()

UserServ = UserService(UserRepository=UserRepo)

async def User_Service_Return() -> UserService:
    return UserServ