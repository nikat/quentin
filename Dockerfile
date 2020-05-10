FROM python:3.8

RUN set -e \
 && pip3 install --upgrade pip \
 && pip3 install aiogram PyYAML aiohttp-socks \
 && echo pip install complete!

WORKDIR /app

ADD config.yml /app/config.yml
ADD main.py /app/main.py

CMD python3 main.py
