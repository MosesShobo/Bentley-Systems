FROM python:3.10-alpine3.19 AS builder

WORKDIR /app

COPY ../requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app/app.py"]  