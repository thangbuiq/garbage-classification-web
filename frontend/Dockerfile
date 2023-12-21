FROM node:16 as builder
USER root
WORKDIR /app

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y libfontconfig1 git && \
    rm -rf /var/lib/apt/lists/*

COPY . .
# Install npm packages
RUN npm install && npm install -g react-scripts && npm install -g axios
ENTRYPOINT ["npm", "run", "build"]