FROM python:3.7-slim
MAINTAINER Ahad
COPY . /docker/Online_Food_Ordering_System/
WORKDIR /docker/Online_Food_Ordering_System/
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
#RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000
CMD ["nohup", "python", "manage.py", "runserver", "0.0.0.0:8000"]