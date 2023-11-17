FROM python:alpine

RUN apk add socat

EXPOSE 1337

CMD cd /app && socat TCP4-LISTEN:1337,fork EXEC:"python3 chal.py"
