import datetime

import jwt
import os

secret_key = "secret"

async def jwt_create(model):
    payload = {"exp_time":str(datetime.datetime.now().date() + datetime.timedelta(days=1)),"login":model.login}
    tok = jwt.encode(payload=payload,key=secret_key,algorithm="HS256")
    print(tok)
    return tok

async def emailjwt_create(model):
    print('START HERE IIIIIIIIIIIIIIII',model.uuid,'END HERE IIIIIIIIIIIIIIIIIII')
    payload = {"uuid":str(model.uuid)}
    tok = jwt.encode(payload=payload,key=secret_key,algorithm="HS256")
    print(type(tok),'AAAAAAAAAAAAAAAABBBBBBBB')
    print(tok,'AAAAAAAAAAAAAAAAAAAA')
    return tok

async def emailjwt_read(token):
    tok = jwt.decode(jwt=token,key=secret_key,algorithms="HS256")
    return tok

