FROM python:3.12-slim

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR app

COPY ./app app

CMD ["python", "./app/main.py"]