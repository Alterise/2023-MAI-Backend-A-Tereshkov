FROM python:3.11

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
