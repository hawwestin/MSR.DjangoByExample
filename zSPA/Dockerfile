FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /zSPA

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /zSPA .
COPY .env .
