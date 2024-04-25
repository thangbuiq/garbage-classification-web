###################################################
#######################WARNING#####################
# We not to use this Dockerfile in production
# This Dockerfile is only for debug purpose
###################################################

FROM python:3.11-alpine
WORKDIR /opt/app
COPY . .
RUN apk add --update alpine-sdk
RUN \
  pip install --upgrade pip
RUN pip install tensorflow
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python3", "main.py" ]
