FROM node:18-alpine

RUN apk add supervisor nginx socat

WORKDIR /app
COPY ./app/package.json ./app/package-lock.json ./
RUN npm ci

COPY ./app ./

COPY nginx.conf /etc/nginx/http.d/default.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf

COPY scripts /

EXPOSE 80
EXPOSE 1337

CMD /setup.sh && supervisord -c /etc/supervisor/supervisord.conf
