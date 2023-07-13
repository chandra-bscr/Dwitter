FROM python:3.9-alpine AS build

WORKDIR /app

ENV $(cat .env | xargs)

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

