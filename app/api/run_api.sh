#!/bin/bash
gunicorn app:app --config python:api.gunicorn_config

