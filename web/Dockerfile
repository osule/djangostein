FROM python:3

RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

COPY . .

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["uwsgi"]