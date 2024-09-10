import datetime

import jwt
import os

secret_key = "secret"

async def jwt_create(model):
    payload = {"exp_time":str(datetime.datetime.now().date() + datetime.timedelta(days=1)),"login":model.login}
    tok = jwt.encode(payload=payload,key=secret_key,algorithm="HS256")
    return tok

async def jwt_check(token):
    tok = jwt.decode(token,key=secret_key,algorithms="HS256")
    time = datetime.datetime.strptime(tok.get("exp_time"),"%Y-%m-%d")
    if datetime.datetime.now() > time:
        return False
    else:
        return True

async def emailjwt_create(model):
    payload = {"uuid":str(model.uuid)}
    tok = jwt.encode(payload=payload,key=secret_key,algorithm="HS256")
    return tok

async def emailjwt_read(token):
    tok = jwt.decode(jwt=token,key=secret_key,algorithms="HS256")
    return tok

