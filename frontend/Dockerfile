FROM node:18.16.0-alpine3.17 AS build
WORKDIR /opt/app
COPY . .
RUN \
  npm install && \
  npm install --save-dev react-scripts
EXPOSE 3000