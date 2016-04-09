# GPUL_RFID
Sistema RFID para apertura de puertas

## Esquema
![Esquema proyecto](https://github.com/AlexPeral/GPUL_RFID/blob/master/Circuito.png "Esquema proyecto")

IP de la raspberry `192.168.13.117`

## Logger
### Instalación
Iniciar el servidor

    cd /srv/rfid_logger_http
    python -m SimpleHTTPServer

### Uso
Crear entradas

    python3 serverdatasource.py

Ejemplo:
[src/logger/logger_example_use.py](https://github.com/AlexPeral/GPUL_RFID/blob/master/src/logger/logger_example_use.py)
