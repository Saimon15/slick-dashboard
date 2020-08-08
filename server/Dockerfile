FROM python:3.8.2

RUN pip install pipenv

COPY ./requirements.txt /app/server/requirements.txt

WORKDIR /app/server

RUN pip install -r requirements.txt

COPY . /app/server

EXPOSE 5000

CMD gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info