FROM python:latest
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir "/auth"

WORKDIR /auth

COPY . /auth

EXPOSE 8000

RUN pip install -r requirements.txt


