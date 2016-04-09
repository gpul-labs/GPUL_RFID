import sys

from MFRC522.MFRC522 import MFRC522
from LCD.lcd import *
import signal
import time

import RPi.GPIO as GPIO

GREEN_LED_PORT = 11

TARJETA_BLANCA = [213,60,214,229,218]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  #MIFAREReader.GPIO_CLEAN()
  GPIO.cleanup()

def init():
  #LED INIT
  GPIO.setwarnings(False) 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(GREEN_LED_PORT, GPIO.OUT)
  GPIO.output(GREEN_LED_PORT, False) 
  #LCD INIT
  lcd_init()

def read():
  MIFAREReader = MFRC522()
  print "Leer Tarjeta, tienes 5 s"
  EndTime = time.time()+5
  while EndTime > time.time():
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    print "hola"
    if status == MIFAREReader.MI_OK:
      print "Card detected"
    #ENCENDER LEED
    (status,backData) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
      print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
      lcd_string("Card Detected  <",LCD_LINE_1)
      Codigo = str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])
      lcd_string(Codigo,LCD_LINE_2)
      GPIO.output(GREEN_LED_PORT, True)
      print "encender led"
      #APAGAR LEED
      time.sleep(3)
      GPIO.output(GREEN_LED_PORT, False)
      lcd_byte(0x01, LCD_CMD,LCD_BACKDARK)
      break
  print "Tiempo lectura expirado"
  
def main():

  init()
  signal.signal(signal.SIGINT, end_read)
  while True:
    read()

if __name__ == '__main__':
  main()
