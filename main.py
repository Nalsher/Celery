import ssl

from fastapi import FastAPI
from endpoints.users_crud import router
from endpoints.table import table_router
from endpoints.mailverification import mail
from email.message import EmailMessage
import smtplib


app = FastAPI()

app.include_router(mail)
app.include_router(router)
app.include_router(table_router)

send_from = 'andriyanworking@gmail.com'
passw = 'kdfn oztg qbmu dgoa'
send_to = 'nalsher228@gmail.com'
subj = 'Hello'
body = """Hello there"""
email = EmailMessage()
email['From'] = send_from
email['To'] = send_to
email['Subject'] = subj
email.set_content(body)
cont = ssl.create_default_context()
@app.get("/get_info")
async def func():
    print('working')
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=cont) as serv:
        serv.login(send_from,passw)
        serv.sendmail(send_from,send_to,'text')
