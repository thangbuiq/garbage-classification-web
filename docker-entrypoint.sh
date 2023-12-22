#!/bin/sh

echo "$0: Starting the application"
cd /opt/aws/bin/
export PUBLIC_IP_ADDRESS=$(curl http://checkip.amazonaws.com)
export PUBLIC_DNS_ADDRESS=$(ec2-metadata -p | grep -oP '(?<=public-hostname: ).*')

# Replace the javascript placeholder with the actual IP address
sed -i "s|PUBLIC_IP_ADDRESS|$PUBLIC_IP_ADDRESS:8000|g" /usr/share/nginx/html/static/js/*.js
cd /app

# Start Nginx in the foreground
nginx -g "daemon off;" &

# Start the Python application
python3 main.py