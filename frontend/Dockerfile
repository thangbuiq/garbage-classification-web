FROM node:16 as builder

ARG DockerUSER=ProEnvUs
ARG DockerUID=2023
ARG DockerGID=2023
ARG DockerPW=docker

USER ${DockerUID}:${DockerGID}
WORKDIR /home/${DockerUSER}
RUN chown -R ${DockerUSER}:${DockerUSER} /home/${DockerUSER}

COPY package*.json .
RUN \
    apt-get update && \
    apt-get install -y libfontconfig1 git && \
    npm install && \
    npm install -g react-scripts