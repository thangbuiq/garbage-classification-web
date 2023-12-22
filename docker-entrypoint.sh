#!/bin/sh

echo "$0: Starting the application"

export PUBLIC_IP_ADDRESS=$(curl http://checkip.amazonaws.com)

# Replace the javascript placeholder with the actual IP address
sed -i "s|PUBLIC_IP_ADDRESS|$PUBLIC_IP_ADDRESS:8000|g" /usr/share/nginx/html/static/js/*.js

# Start Nginx in the foreground
nginx -g "daemon off;" &

# Start the Python application
python3 main.py