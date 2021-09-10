#!/bin/bash
# This script is used to book the Docker container for this app

source sbvenv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "Deploy command failed, retrying in 5 seconds..."
    sleep 5
done
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - shayblog:app