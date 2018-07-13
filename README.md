[![CircleCI](https://circleci.com/gh/tsoporan/fittrak/tree/master.svg?style=svg)](https://circleci.com/gh/tsoporan/fittrak/tree/master)

A no-frills fitness tracking tool for the stats inclined.

### Requirements

- [Python](https://www.python.org/) 3.6
- [pipenv](https://github.com/pypa/pipenv)
- [yarn](https://yarnpkg.com/en/)

### Set up

The backend consists of a [Django](https://www.djangoproject.com/) powered Python application which exposes a 
[GraphQL](https://graphql.org/learn/) API using [Graphene](http://graphene-python.org/).

To get it up and running:

1. Install required packages
```bash
pipenv install
pipenv shell
cd fittrak
```

2. Configure secrets
```bash
echo SECRET_KEY=\"PlsChangeMe\" > fittrak/secrets.py
echo HASHIDS_SALT=\"AndMe\" >> fittrak/secrets.py
```

3. Initial migration
```bash
./manage.py migrate
```

4. Set up the first user and load some fixture data
```bash
./manage.py createsuperuser
./manage.py loaddata workout
```

5. Tests
```bash
./manage.py test
```

6. Dev
```bash
./manage.py runserver_plus # Werkzeug dev server
```

---

The frontend is a [Vue](https://vuejs.org/) powered Javascript application which uses [Apollo](https://www.apollographql.com/) as its GraphQL
client.

For local dev the **backend** must be up and running as that is where the graphql server runs (requests to
`/graphql` will fail otherwise!) For dev purposes `corsheaders` is being used so frontend dev can
happen "painlessly" while in production, `yarn build`, will output the files so Django can use them.

**NOTE** `yarn serve` will overwrite the assets from `yarn build` currently which will not work as
expected.

To get it up and running:

1. Install required packages
```bash
cd fittrak-client
yarn install
```

2. Tests
```bash
yarn test:unit
```

3. Dev hot reloaded
```bash
yarn serve
```

4. Production, note the output path
```bash
yarn build
```
