#!/bin/bash
# Run migrations and start up the dev server

cd fittrak

echo "Starting dev server ..."
./manage.py runserver 0.0.0.0:8000 --settings=fittrak.settings
