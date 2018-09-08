[![CircleCI](https://circleci.com/gh/tsoporan/fittrak/tree/master.svg?style=svg)](https://circleci.com/gh/tsoporan/fittrak/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cacf93b3fc73458c8f51b02b177e07d4)](https://www.codacy.com/app/titus/fittrak?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tsoporan/fittrak&amp;utm_campaign=Badge_Grade)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A no-frills fitness tracking tool for the stats inclined 🤓.

---

### Requirements

For local dev you'll only require:

- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

#### Backend

The backend consists of a [Django](https://www.djangoproject.com/) powered Python application which exposes a [GraphQL](https://graphql.org/learn/) API using [Graphene](http://graphene-python.org/). Django is being used to deal with
authentication, and other various functions, and as such there are some views which are rendered from Django. You may think of Django renders the template which houses the frontend SPA.

#### Frontend

The frontend is a [Vue](https://vuejs.org/) powered Javascript application which uses [Apollo](https://www.apollographql.com/) as a GraphQL client. When deployed in production this simply makes API calls to `/graphql` and benefits from the rest of the Django machinery.

**NOTE**: For local dev the **backend** must be up and running as that is where the API (GraphQL server) runs (requests to
`/graphql` will fail otherwise!) Authentication is based on sessions with IDs stored on cookies, which will be on `localhost` in dev, this works fine as only the ports change between the two servers. Keep an eye out for issues pertaining to authentication as the default behaviour, at the moment, is to return a `302`, rediret to `/login`, which will present an error on the frontend console.

---

### Development

The preferred way to bring up the stack is using `docker-compose`.

First time:
```bash
git clone git@github.com:tsoporan/fittrak.git && cd fittrak

# Bring up only the API to run migrations
docker-compose up api
docker-compose run api python fittrak/manage.py migrate

# Create the first user (admin)
docker-compose run api python fittrak/manage.py createsuperuser

# Bring up everything
docker-compose down && docker-compose up
```

Otherwise:
```
docker-compose up
```

You can also run everything independently, which would require: `postgresql`, `yarn`, `python3.7` and `pipenv`.
With docker we can conveniently package these up and not worry about external deps.

**NOTE:** When running independently make sure you're aware of the env variables required, i.e:
```bash
# Backend
DJANGO_SECRET_KEY=
DJANGO_HASHIDS_SALT=
DJANGO_DEBUG=True
./manage.py runserve_plus

# Frontend
VUE_API_URL=http://localhost:8000/graphql yarn serve
```

There are three services that comprise the stack: `api`, `app`, and `db`. `docker-compose up` brings
them all up though you may start each one with their respective `docker-compose up <serivce>`
command.

It is also useful to know how to work with `docker` and `docker-compose` as you may need to rebuild
and interact with containers during dev.

#### Migrations

To apply DB migrations we can run a command in the container:

- `docker-compose run api python fittrak/manage.py makemigrations`
- `docker-compose run api python fittrak/manage.py migrate`

#### Tests

Tests can be run with the usual:

- `docker-compose run api python fittrak/manage.py test`

---

### Deployment

Firstly check how the app behaves in production mode:

```bash

# Build production bundle

cd fittrak-client
NODE_ENV=production yarn build

# This will dump the assets in ../fittrak/assets which will be picked up
# by the "render_bundle" template tag in Django

# Set DEBUG to "False" in docker-compose
docker-compose up

# Visit http://localhost:8000
```


The application currently sits on a [GCP VM](https://cloud.google.com/compute) and uses [Cloud SQL](https://cloud.google.com/sql/) (PostgreSQL 9.6). SSL is through [LetsEncrypt](https://letsencrypt.org/) and the Nginx [Certbot](https://certbot.eff.org/lets-encrypt/ubuntuartful-nginx.html)

Future plans may include IaC, and moving to a more robust container solution, such as k8s, though it's fairly overkill at the moment.
