#!/usr/bin/env bash
python mysite/manage.py migrate datasets zero
rm -rf mysite/datasets/migrations/
python mysite/manage.py makemigrations datasets
python mysite/manage.py migrate