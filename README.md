# GPUL_RFID
Sistema RFID para apertura de puertas

IP de la raspberry `192.168.13.117`

## Logger
### Instalación
* Entrar en la carpeta del rfid_logger_http `cd /srv/rfid_logger_http`
* Iniciar el servidor `python -m SimpleHTTPServer`

### Uso
* Crear entradas `python3 serverdatasource.py`

Ejemplo:
[src/logger/logger_example_use.py](https://github.com/AlexPeral/GPUL_RFID/blob/master/src/logger/logger_example_use.py)
