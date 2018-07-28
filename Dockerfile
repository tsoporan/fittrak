# Dockerfile for fittrak python

FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock . ./

# Required psql deps
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install pipenv && \
 pipenv install --system --ignore-pipfile && \
 apk --purge del .build-deps

EXPOSE 8000

CMD ["sh", "start.sh"]
