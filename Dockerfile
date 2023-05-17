FROM yak
ENV PYTHONUNBUFFERED 1

WORKDIR /app

USER root


CMD pwd

CMD uwsgi --ini uwsgi.ini
