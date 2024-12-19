FROM python:3.10-alpine AS base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache build-base git

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . ./

CMD ["python", "src/main.py"]
