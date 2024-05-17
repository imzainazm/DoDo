FROM python:3.12.3-alpine3.19

WORKDIR /app

COPY requirements.txt /app

RUN apk update && \
    apk upgrade && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
