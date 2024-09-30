FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip
COPY requirements.txt /app_dev/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "python manage.py migrate && python manage.py loaddata data.json && python manage.py runserver 0.0.0.0:8000"]
