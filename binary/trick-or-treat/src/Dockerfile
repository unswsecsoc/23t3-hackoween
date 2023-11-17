FROM ubuntu:latest

EXPOSE 9999

RUN apt-get update && apt-get install -y socat \
	&& apt-get install -y gcc \
	&& apt-get install -y make

WORKDIR /app

COPY ./trick-or-treat.c ./flag.txt ./Makefile ./
RUN cd /app && make

CMD socat TCP4-LISTEN:9999,fork EXEC:/app/trick-or-treat
