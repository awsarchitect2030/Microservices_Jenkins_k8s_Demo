FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 5003

CMD ["python", "app.py"]
