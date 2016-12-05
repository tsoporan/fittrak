### Useful documentation

#### Frontend
- Vuejs https://vuejs.org/v2/guide/
- Vue Router https://router.vuejs.org/en/essentials/getting-started.html
- Vue Resource (http utils) https://github.com/pagekit/vue-resource
- Vuex (state management) https://vuex.vuejs.org/en/intro.html

#### Backend
- Django https://www.djangoproject.com/start/
- Django REST Framework (API) http://www.django-rest-framework.org/tutorial/quickstart/
- JSON Web tokens https://getblimp.github.io/django-rest-framework-jwt/

### Requirements

- Nodejs v7+ / NPM v4+
- Python3 / pip3
- virtualenv

On mac you'll find these all using Homebrew (brew command)

### Getting up and running

After installing the required packages clone the repository, the repository contains two directories one for the api and the other for the client.

#### Setting up API server

0. Create a virtualenv: ```virtualenv envs/fittrack```

1. Activate env: ```cd fittrack_api && source ../envs/fittrack/bin/activate```

2. Install packages: ```pip3 install -r requirements.txt```

3. Run migrations: ```./manage.py migrate```

4. Load fixture data: ```./manage.py loaddata workouts/fixtures/exercises.json```

5. Start up dev server: ```./manage.py runserver_plus```

6. Create a dummy user: ```./manage.py createsuperuser```

7. Server up on: http://localhost:8000

#### Setting up client server

0. Install node packages: ```cd fittrack_client && npm install```

1. Start up the dev server: ```npm run dev```

2. Server up on: http://localhost:8080

---

The client server is live-reload - it will update as you make changes. The API server requires page refresh, but otherwise picks up new code changes.
