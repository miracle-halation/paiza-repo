FROM python:3

USER root
WORKDIR /src

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo

RUN pip install --upgrade pip
COPY ./src/requirements.txt ./
RUN pip install -r requirements.txt

