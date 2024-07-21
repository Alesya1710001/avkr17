FROM tiangolo/uwsgi-nginx-flask:python3.11
LABEL maintainer="Alesya Krop <kropka171001@gmail.com>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV NGINX_WORKER_PROCESSES auto

COPY . /app

RUN pip install -U pip
RUN pip install -r requirements.txt

ENV TZ=Europe/Minsk

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]


