#!/bin/sh

# Start Nginx in the foreground
nginx -g "daemon off;" &

# Start the Python application
python3 main.py