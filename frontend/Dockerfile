# Stage 1: Build
FROM node:16 as builder
WORKDIR /opt/app
COPY . .
RUN \
    apt-get update && \
    apt-get install -y libfontconfig1 git && \
    npm install && \
    npm install --save-dev react-scripts && \
    npm run build

# Stage 2: Serve using Nginx
FROM nginx:alpine
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /opt/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
