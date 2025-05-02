FROM python:3.13-alpine AS base
WORKDIR /api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py .
ENTRYPOINT ["fastapi", "run", "main.py"]
