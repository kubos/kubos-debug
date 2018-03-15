#!/bin/bash

gunicorn index:app -b 0.0.0.0:52861 -t 360
