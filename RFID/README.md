# Schema
![Esquema RFID](https://github.com/AlexPeral/GPUL_RFID/blob/master/RFID/Diagrama.jpeg "Esquema RFID")


## Config
Module RFID-RC522

### Install python-dev

    sudo apt-get install python-dev

### Enable device tree

    echo device_tree=on >> /boot/config.txt

### Enable SPI

    sudo raspi-config

select advance options
Select A6 SPI  Enable/Disable automatic loading and say yes to all the options.

Reboot the system and you should see spidev0.0 and spidev0.1 in dev

### Install BCM2835

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

### Install SPI-Py Library

    git clone https://github.com/lthiery/SPI-Py.git
    cd SPI-Py
    sudo python setup.py install


## Running

Install MFRC522

    git clone https://github.com/rasplay/MFRC522-python.git
    cd MFRC522-python
    sudo python Read.py
