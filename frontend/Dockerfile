# STAGE 1
FROM node:16 as builder
USER root
WORKDIR /app
RUN apt-get update && \
    apt-get install -y libfontconfig1 git && \
    rm -rf /var/lib/apt/lists/*
COPY . .
RUN npm install && npm install -g react-scripts && npm install -g axios
RUN npm run build
# STAGE 2
FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80