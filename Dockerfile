# Dockerfile for fittrak python app

FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Required psql deps
RUN apt-get update \
  && apt-get install postgresql-client -y \
  && pip install pip -U \
  && pip install pipenv

COPY Pipfile Pipfile.lock . ./

RUN pipenv install --system --ignore-pipfile

EXPOSE 8000

CMD ["sh", "scripts/start.sh"]
