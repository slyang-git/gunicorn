#!/usr/bin/env bash

bin/gunicorn --workers 1 --log-level=debug wsgi
