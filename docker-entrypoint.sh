#!/bin/sh

echo "$0: Starting the application"

export PUBLIC_IP_ADDRESS=$(curl http://checkip.amazonaws.com)

# Start Nginx in the foreground
nginx -g "daemon off;" &

# Start the Python application
python3 main.py