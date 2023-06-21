FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

#CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000 & python update_data.py"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]