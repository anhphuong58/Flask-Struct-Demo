FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000
ENV PORT 5000

CMD exec gunicorn --reload --bind :$PORT main:app --workers 1 --threads 1 --timeout 60
