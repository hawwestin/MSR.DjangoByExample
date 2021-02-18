FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

RUN apk add --update --no-cache --virtual .tmp \
gcc libc-dev linux-headers python3-dev \
musl-dev \
&& apk add --no-cache jpeg-dev zlib-dev \
&& apk add --no-cache mariadb-dev \
&& apk add --no-cache dos2unix

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk del .tmp

RUN mkdir /zSPA
COPY ./zSPA /zSPA

WORKDIR /zSPA

COPY ./scripts /scripts 
COPY .env ./.env

RUN dos2unix * /scripts/*

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user

RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user

CMD ["entrypoint.sh"]
