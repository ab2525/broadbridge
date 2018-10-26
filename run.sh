#!/bin/bash

# Update this to your installation path
FLASK_APP=/opt/broadbridge/application.py
HOST=0.0.0.0 #What IP to listen on, default - all
PORT=5453 #What port to listen on, default - 5453

/usr/local/bin/flask run -h "$HOST" -p "$PORT"
