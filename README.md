# GPUL_RFID

Sistema RFID para apertura de puertas


sensor rfid: RFID-RC522
ip de la raspberry 192.168.13.117


sources:

http://fuenteabierta.teubi.co/2013/07/utilizando-el-lector-nfc-rc522-en-la.html


<h1>Init and use Logger module.</h1>

1- start python server to server results.
cd /srv/rfid_logger_http
python -m SimpleHTTPServer

2- Provide log entries to http server with:
python3 serverdatasoruce.py

3- use class logger, see src/logger/logger_example_use.py