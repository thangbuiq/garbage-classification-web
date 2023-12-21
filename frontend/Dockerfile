FROM node:16 as builder

ARG DockerUSER=ProEnvUs
ARG DockerUID=2023
ARG DockerGID=2023
ARG DockerPW=docker

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y libfontconfig1 git && \
    rm -rf /var/lib/apt/lists/*

# Switch back to your specified user
USER ${DockerUID}:${DockerGID}
WORKDIR /home/${DockerUSER}

# Set ownership
RUN chown -R ${DockerUID}:${DockerGID} /home/${DockerUSER}

# Copy package.json files and install npm packages
COPY package*.json .
RUN npm install && \
    npm install -g react-scripts
