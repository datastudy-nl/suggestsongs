FROM python:3.12-slim

ARG GH_PAT
ARG GITHUB_ACTOR

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git python3-pop

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
