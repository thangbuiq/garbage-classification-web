FROM node:16 as builder

ARG DockerUSER=ProEnvUs
ARG DockerUID=2023
ARG DockerGID=2023
ARG DockerPW=docker

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y libfontconfig1 git && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for the application and set permissions
RUN mkdir -p /home/${DockerUSER} && \
    chown -R ${DockerUID}:${DockerGID} /home/${DockerUSER}

WORKDIR /home/${DockerUSER}
COPY package*.json .
RUN chown ${DockerUID}:${DockerGID} package*.json

# Install npm packages
RUN npm install && \
    npm install -g react-scripts
