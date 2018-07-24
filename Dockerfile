# Dockerfile for fittrak python

FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock . ./

RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile

EXPOSE 8000

CMD ["sh", "start_gunicorn.sh"]
