from celery import Celery
import smtplib
from email.message import EmailMessage
from users.jt.tokens import emailjwt_create


celery = Celery('CeleryTask',broker="redis://redis:6379")

async def create_message(model):
    email = EmailMessage()
    email['From'] = 'andriyanworking@gmail.com'
    email['To'] = model.email
    email['Subject'] = 'E-mail verfication'
    return email

@celery.task
async def send_message(model):
    send_from = "andriyanworking@gmail.com"
    password = "Nalsher2"
    mail = await create_message(model)
    mailjwt = await emailjwt_create(model)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as serv:
        serv.login(send_from,'kdfn oztg qbmu dgoa')
        serv.sendmail(send_from,model.email,f"To verify your account click this link\n"
                                            f"0.0.0.0:8001/email/{mailjwt}")
