FROM pypy:3-slim

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install twisted pendulum
