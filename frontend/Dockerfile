FROM node:16 as builder
WORKDIR /opt/app
COPY package*.json .
RUN \
    apt-get update && \
    apt-get install -y libfontconfig1 git && \
    npm install && \
    npm install --save-dev react-scripts