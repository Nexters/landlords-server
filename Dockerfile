FROM python:3.8-alpine

# -- timezone sync
RUN set -ex && apk update \
    && apk add tzdata \
    && cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone \
    && apk del tzdata

# build-base: gevent dependency
# libffi-dev: bcrypt dependency
RUN set -ex && apk update \
    && apk add build-base libffi-dev libressl-dev openssl-dev musl-dev\
    && rm -rf /var/cache/apk/*

RUN set -ex \
    && pip3 install --upgrade pip \
    && pip3 install pipenv


# -- install dependency with pip
COPY requirements.txt requirements.txt
RUN set -ex & pip install -r requirements.txt
RUN apk del build-base libffi-dev libressl-dev openssl-dev musl-dev

# -- Install Application into container:
COPY src src

CMD exec uvicorn src.asgi:asgi --host 0.0.0.0 --port $PORT
