#!/usr/bin/env bash
python mysite/manage.py makemigrations datasets
python mysite/manage.py migrate