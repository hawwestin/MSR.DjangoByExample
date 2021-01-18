FROM python:3.7.9

# create and set working directory
RUN mkdir /app
WORKDIR /app
# WORKDIR /zSPA


# 
ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8
ENV PORT=8000
EXPOSE $PORT

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \        
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip3 install --upgrade pip 
#RUN pip3 install pipenv

COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

COPY /zSPA .
COPY .env .

CMD gunicorn zSPA.wsgi:application --bind 0.0.0.0:$PORT