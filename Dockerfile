# This Dockerfile is used to build an image containing Errbot
FROM python:3
MAINTAINER Axial_Devops

# Make sure the package repository is up to date.
RUN apt update && apt upgrade -y && \
    apt install python-dev python-pip libyaml-dev libffi-dev libssl-dev unzip wget -y && \
    pip3 install -U python-jenkins errbot six setuptools boto3 slackclient raven pymongo tabulate entr pytest

COPY config.py /err/config.py
COPY extra /err/extra

VOLUME ["/err"]
WORKDIR /err
#ENTRYPOINT ["/usr/local/bin/errbot"]
