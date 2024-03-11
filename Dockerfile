FROM python:3.12-slim

ARG GH_PAT
ARG GITHUB_ACTOR

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
