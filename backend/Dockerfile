###################################################
#######################WARNING#####################
# We not to use this Dockerfile in production
# This Dockerfile is only for debug purpose
###################################################

FROM python:3.11-slim
WORKDIR /opt/app
COPY . .
RUN apt-get update -qq && apt-get install -y build-essential
RUN \
  pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "main:app" ]
