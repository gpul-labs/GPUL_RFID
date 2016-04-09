# Información
* Module RFID-RC522

# Fuentes
http://fuenteabierta.teubi.co/2013/07/utilizando-el-lector-nfc-rc522-en-la.html

# Esquema
![Esquema RFID](https://github.com/AlexPeral/GPUL_RFID/blob/master/RFID/Diagrama.jpeg "Esquema RFID")


# Instalación y configuración
## Instalar python dev tools

    sudo apt-get install python-dev

## Habilitar `device tree`

    echo device_tree=on >> /boot/config.txt

## Habilitar SPI

    sudo raspi-config

Seleccionar opciones avanzadas -> A6 SPI -> Habilitar/Deshabilitar carga automática y sí a todo.

Reboot the system and you should see spidev0.0 and spidev0.1 in dev

### Instalar BCM2835

http://www.airspayce.com/mikem/bcm2835/

```
curl -O http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz
tar zxvf bcm2835-1.xx.tar.gz
cd bcm2835-1.xx
./configure
make
sudo make check
sudo make install
```

### Instalar la librería SPI-Py

    git clone https://github.com/lthiery/SPI-Py.git
    cd SPI-Py
    sudo python setup.py install


## Uso

    git clone https://github.com/rasplay/MFRC522-python.git
    cd MFRC522-python
    sudo python Read.py
