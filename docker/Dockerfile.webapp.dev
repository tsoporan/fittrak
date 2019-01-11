# Dockerfile for fittrak python app (development)

FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock . ./

# Required psql deps
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install pipenv && \
 pipenv install --system --ignore-pipfile --dev && \
 apk --purge del .build-deps

EXPOSE 8000

CMD ["sh", "scripts/start.sh"]
