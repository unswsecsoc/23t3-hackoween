FROM alpine:latest

EXPOSE 9999

RUN apk add binutils
RUN apk add gcc
RUN apk add musl-dev
RUN apk add python3
RUN apk add py3-pip
RUN pip install quart

WORKDIR /app

COPY ./server.py ./index.html ./
COPY ./flag.txt /funni/directory/that/you/will/never/find/

CMD python server.py 9999
