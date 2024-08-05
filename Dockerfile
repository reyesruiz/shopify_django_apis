FROM python:3

WORKDIR /usr/src/app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt update;apt upgrade -y
RUN mkdir /var/log/gunicorn/
RUN mkdir /var/run/gunicorn/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
