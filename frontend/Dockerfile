FROM node:16 as builder

ARG DockerUSER=ProEnvUs
ARG DockerUID=2023
ARG DockerGID=2023
ARG DockerPW=docker
RUN \
    groupadd --gid=${DockerGID} ${DockerUSER} && \
    useradd --no-log-init --create-home ${DockerUSER} --uid=${DockerUID} --gid=${DockerGID} && \
    echo "${DockerUSER}:${DockerPW}" | chpasswd && \
    usermod -aG sudo ${DockerUSER}

USER ${DockerUID}:${DockerGID}
WORKDIR /home/${DockerUSER}
COPY package*.json .
RUN \
    apt-get update && \
    apt-get install -y libfontconfig1 git && \
    npm install && \
    npm install -g react-scripts