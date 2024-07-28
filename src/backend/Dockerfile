#TODO: find better base image
FROM python:3.12.4

WORKDIR /app
USER root

RUN mkdir /app/comms \
   && mkdir /app/util
RUN mkdir /app/data \
   && mkdir /app/log

COPY *.py ./
COPY ./comms/*.py ./comms/
COPY ./util/*.py ./util/
COPY ./enums/*.py ./enums/
COPY ./prompts/*.py ./prompts/
COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y \
   && apt-get install vim -y \
   && apt-get install curl -y \
   && apt-get install ffmpeg -y \
   && pip3 install -r requirements.txt

RUN chown -R 1001:1001 /app/
RUN chmod 755 /app/

USER 1001
CMD ["fastapi", "run", "api.py"]