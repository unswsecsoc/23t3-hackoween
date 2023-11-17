FROM ubuntu:latest

EXPOSE 9999

RUN apt-get update && apt-get install -y socat \
	&& apt-get install -y gcc \
	&& apt-get install -y libseccomp-dev \
	&& apt-get install -y gdb \
	&& apt-get install -y make

COPY ./flag.txt /
WORKDIR /app

COPY ./whispers.c ./flag.txt ./Makefile ./
RUN cd /app && make

CMD socat TCP4-LISTEN:9999,fork EXEC:/app/whispers
