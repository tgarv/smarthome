#!/bin/bash

source /home/pi/projects/smart_home/venv/bin/activate
export FLASK_APP=/home/pi/projects/smart_home/app/app.py
flask run --host=0.0.0.0
