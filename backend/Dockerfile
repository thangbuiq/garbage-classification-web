FROM node:18.16.0-alpine3.17 AS build
WORKDIR /opt/app
COPY package*.json .
RUN \
  npm install && \
  npm install --save-dev nodemon
EXPOSE 5000