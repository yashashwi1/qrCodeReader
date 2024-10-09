From ubuntu:jammy
#FROM ubuntu/python:3.10-22.04_stable
#FROM python:3.9.20-slim

RUN apt-get update \
     #   && apt-get dist-upgrade --no-install-recommends -y \
      #  && apt-get install --no-install-recommends -y apt-utils \
        && apt-get upgrade --no-install-recommends -y \
        && apt-get install --no-install-recommends -y \
        ffmpeg \
        libsm6 \
        libxext6 \
        python3 \
        python3-pip \
        #pip install qreader \
        libzbar0
RUN apt-get clean
RUN pip install qreader
#RUN pip install -r /src/requirements.txt
#RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y clean all
#RUN apt install python3 -y clean all
#RUN python --version
#RUN exit
#RUN apt install python3.8-venv -y
#RUN python3 -m venv abc
#RUN sudo /abc/bin/activate
#RUN apt-get install python3-pip -y clean all

#RUN pip install qreader
#RUN apt-get install libzbar0 -y
COPY src /src
RUN ls -la
WORKDIR /src
RUN ls -la
#USER root                                 #RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt
#RUN mkdir -p /src/qrOutput
#WORKDIR /src/qrOutput
USER root
ENTRYPOINT ["sh", "-c", "python3 qrCodeReader.py 1"]
