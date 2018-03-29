#!/bin/bash

gunicorn index:app -b '[::]:52861' -t 360
