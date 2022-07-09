FROM python:latest

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 8888

CMD ["python", "./main.py"]