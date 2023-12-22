# STAGE 1
FROM node:16-alpine as builder
USER root
WORKDIR /app
COPY frontend/ .
ARG PUBLIC_IP_ADDRESS=localhost
ENV PUBLIC_IP_ADDRESS=${PUBLIC_IP_ADDRESS}
RUN \
    npm install && \
    npm install -g react-scripts && \
    npm install -g axios
RUN npm run build

# STAGE 2
FROM tiangolo/uwsgi-nginx:python3.11
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
WORKDIR /app
COPY backend/ .
RUN \
  pip install --upgrade pip && \
  pip install -r ./requirements.txt
EXPOSE 8000
COPY ./docker-entrypoint.sh .
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]