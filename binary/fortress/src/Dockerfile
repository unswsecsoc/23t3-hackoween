FROM ubuntu:latest

EXPOSE 9999

RUN apt update -y
RUN apt install socat gcc -y

WORKDIR /app

COPY ./challenge.c ./flag.txt ./

# -no-pie to make leaking the binary easier (known base address).
RUN gcc challenge.c -g -no-pie

CMD socat TCP4-LISTEN:9999,fork EXEC:/app/a.out
