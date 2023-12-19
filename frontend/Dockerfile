FROM node:18.16.0-alpine3.17 AS build
WORKDIR /opt/app
COPY . .
RUN npm install
EXPOSE 3000
CMD [ "npm", "run", "start" ]