FROM python:3.10.12-alpine3.17
WORKDIR /opt/app
COPY requirements.txt .
RUN \
  pip install --upgrade pip \
  && pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]