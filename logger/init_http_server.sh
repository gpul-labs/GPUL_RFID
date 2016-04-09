#!/usr/bin/env bash
cd /srv/rfid_logger_http
python -m SimpleHTTPServer
python3 serverdatasoruce.py &