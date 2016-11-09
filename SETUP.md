### Requirements

- Nodejs/NPM
- Python 3
- virtualenv

On mac you'll find these all using Homebrew (brew command)

### Getting Up and Running

After installing the required packages clone the repository, the repository contains two directories one for the api and the other for the client.

#### Setting up api server

0. Create a virtualenv: ```virtualenv envs/fittrack```

1. Activate env: ```cd fittrack_api && source ../envs/fittrack/bin/activate```

2. Install packages: ```pip3 install -r requirements.txt```

3. Run migrations: ```./manage.py migrate```

4. Load fixture data: ```./manage.py loaddata workouts/fixtures/exercises.json```

5. Start up dev server: ```./manage.py runserver_plus```

6. Create a dummy user: ```./manage.py createsuperuser```

7. Server up on: http://localhost:8000

### Setting up client server

0. Install node packages: ```cd fittrack_client && npm install```

1. Start up the dev server: ```npm run dev```

2. Server up on: http://localhost:8080

---

The client server is live-reload - it will update as you make changes. The API server requires page refresh, but otherwise picks up new code changes.
