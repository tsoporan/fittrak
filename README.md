[![CircleCI](https://circleci.com/gh/tsoporan/fittrack/tree/master.svg?style=shield)](https://circleci.com/gh/tsoporan/fittrack/tree/master)

A no-frills fitness tracking tool for the stats inclined.

### Requirements

- `pipenv`
- `yarn`

### Set up

**Backend**: The backend consists of a Django powered Python application which exposes a 
GraphQL API using Graphene.

To get it up and running:

1. Install required packages
```bash
cd backend
pipenv shell
pipenv install
```

2. Configure a `SECRET_KEY`
```bash
echo SECRET_KEY=\"PlsChangeMe\" > fittrak/secrets.py
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

4. Serve
```bash
./manage.py runserver
```

---

**Frontend**: The frontend is a Vue powered Javascript application which uses Apollo as its GraphQL
client.

To get it up and running:

1. TBD
