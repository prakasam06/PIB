FROM ubuntu:18.04

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update
RUN apt install -y python3-pip
RUN apt-get -y install tesseract-ocr
COPY requirements.txt /usr/src/app/
RUN pip3 install --default-timeout=100 --no-cache-dir -r requirements.txt
COPY . /usr/src/app

