#TODO: find better base image
FROM ubuntu:latest

WORKDIR /app/path
USER root

RUN mkdir /app/path/comms

COPY *.py .
COPY ./comms/*.py ./comms/
COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y \
   && apt-get install vim -y \
   && apt-get install python3-pip -y \
   && pip3 install -r requirements.txt

RUN chown -R 1001:1001 /app/path
RUN chmod 755 /app/path

USER 1001
CMD ["fastapi", "api.py"]