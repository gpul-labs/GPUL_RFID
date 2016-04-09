import sys

from MFRC522.MFRC522 import MFRC522
from LCD.lcd import *
from dao.carddao import CardsDAO
from dao.loggerdao import LoggerDAO
from proxsensor.sensor import ProxSensor
from logger.httpserverdatasource import HTTPServerDatasource
import signal
import time
import threading
import RPi.GPIO as GPIO
import picamera

GREEN_LED_PORT = 11
RED_LED_PORT = 13
YELLOW_LED_PORT = 15


class RFID(object):
      
  def __init__(self):

    # interceptar signaling

    signal.signal(signal.SIGTERM, self.handle_shutdown)
    signal.signal(signal.SIGINT, self.handle_shutdown)

    #LED INIT
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GREEN_LED_PORT, GPIO.OUT)
    GPIO.output(GREEN_LED_PORT, False) 
    GPIO.setup(RED_LED_PORT, GPIO.OUT)
    GPIO.output(RED_LED_PORT, False)
    GPIO.setup(YELLOW_LED_PORT, GPIO.OUT)
    GPIO.output(YELLOW_LED_PORT, False) 
    #LCD INIT
    lcd_init()
    #DAO INIT
    self.cardDao=CardsDAO()
    self.loggerDao=LoggerDAO()
    #Proximite Sensor Init
    self.proxsensor = ProxSensor()
    ## ipc para thread http server
    self.ipc_logger = threading.Event()
    self.ipc_logger.set()
     ## ipc para main
    self.ipc_main = threading.Event()
    self.ipc_main.set()
    self.http_server_ds=HTTPServerDatasource(self.ipc_logger)
    #Cargar camara
    self.camera= picamera.PiCamera()


    threading.Thread(target=self.http_server_ds.run).start()

  def handle_shutdown(self, num=None, frame=None):

    self.ipc_logger.clear()
    time.sleep(2)
    self.ipc_main.clear()


  def _checkCard(self,Data):
    Card=self.cardDao.get_card(Data[0],Data[1],Data[2],Data[3],Data[4])
    if Card is not None:
      return Card['username']
    else:
      return None


  def _codigoToString(self,backData):
    return str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])

  def _codigoToFormatedString(self,backData):
    return str(backData[0])+"."+str(backData[1])+"."+str(backData[2])+"."+str(backData[3])+"."+str(backData[4])

  def _printLCD(self,Line1,Line2):
     lcd_string(Line1,LCD_LINE_1)
     lcd_string(Line2,LCD_LINE_2)

  def _formatName(self,Nombre):
    return Nombre[0].upper()+Nombre[1:].lower()

  def _BeforeWait(self,Nombre):
    self._printLCD("Access Granted","Welcome "+self._formatName(Nombre))
    GPIO.output(GREEN_LED_PORT, True)

  def _AfterWait(self):
    GPIO.output(GREEN_LED_PORT, False)
    lcd_byte(0x01, LCD_CMD,LCD_BACKDARK)
    

  def read(self):
    MIFAREReader = MFRC522()
    print "Reading card, have 5 s"
    EndTime = time.time()+5
    while EndTime > time.time():
      (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
      print "checking"
      if status == MIFAREReader.MI_OK:
        print "Card detected"
      #ENCENDER LEED
      (status,backData) = MIFAREReader.MFRC522_Anticoll()
      if status == MIFAREReader.MI_OK:
        print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
        user=self._checkCard(backData)
        if user is None:
          print"Access Denied"
          self.loggerDao.log_entry("Access Denied, ID "+self._codigoToFormatedString(backData))
          self._printLCD("Access Denied",self._codigoToString(backData))
          GPIO.output(RED_LED_PORT, True)
          time.sleep(3)
          GPIO.output(RED_LED_PORT, False)
          lcd_byte(0x01, LCD_CMD,LCD_BACKDARK)
          break
        else:
          print "Access Granted"
          self.loggerDao.log_entry("Access Granted, User: "+user+" Card "+self._codigoToFormatedString(backData))
          self._BeforeWait(user)
          time.sleep(3)
          self._AfterWait()
          break
    print "Reading Timeout"


  def run(self):

    while self.ipc_main.is_set():
      print "midiendo"
      Medida =  self.proxsensor.medir()
      print Medida
      if Medida <10:        
        self.loggerDao.log_entry("Presencia detectada")
        GPIO.output(YELLOW_LED_PORT, True)
        self._printLCD("Pasa La Tarjeta","Tienes 5 seg")
        self.camera.capture('/srv/rfid_logger_http/capture.jpg')
        self.read()
        GPIO.output(YELLOW_LED_PORT, False)
      time.sleep(1)
    lcd_byte(0x01, LCD_CMD,LCD_BACKDARK)
    print "Proceso Finalizado"


# BOB 213,60,214,229,218
# Alice 148,209,91,46,48
def main():
  rfid=RFID()
  rfid.run()


if __name__ == '__main__':
  main()
