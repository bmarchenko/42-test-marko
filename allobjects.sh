#!/bin/bash

python manage.py allobjects 2> "$( date +"%Y-%m-%d" ).dat"
