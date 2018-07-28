#!/bin/bash
# Start up gunicorn

cd fittrak

gunicorn fittrak.wsgi:application -b 0.0.0.0:8000
