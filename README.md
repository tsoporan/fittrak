[![CircleCI](https://circleci.com/gh/tsoporan/fittrak/tree/master.svg?style=svg)](https://circleci.com/gh/tsoporan/fittrak/tree/master)

A no-frills fitness tracking tool for the stats inclined.

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

The preferred way to bring up the stack is using `docker-compose`. If you really wanted to you
could also run everything independently, which would require: `postgresql`, `yarn`, `python3.7` and `pipenv`.
With docker we can conveniently package these up and not worry about external deps.

There are three services that comprise the stack, you can bring them all up with `docker-compose up`,
which will start all three: `api`, `db` and `app` (you can bring them up indepdently with the
respective `docker-compose up <service>` command). 

It is also useful to know how to work with `docker` and `docker-compose` as you may need to rebuild 
and interact with containers during dev.

#### Migrations

To apply DB migrations we can run a command in the container:

- `docker-compose run api python fittrak/manage.py makemigrations`
- `docker-compose run api python fittrak/manage.py migrate`

#### Tests

Tests can be run with the usual: 

- `docker-compose run api python fittrak/manage.py test`

#### First time set up

The first time will be slightly different as you'll want to set up the DB and create an initial user.

1. Run migrations (mentioned above)

2. Create a super user: `docker-compose run api python fittrak/manage.py createsuperuser`

3. Load up fixture data: `docker-compose run api python fittrak/manage.py loaddata workout`

---

### Deployment

The application has been vetted on GCP using Kubernetes, you'll notice that there are some manifest
files in the `infra` directory though this is still largely a work in progress.
