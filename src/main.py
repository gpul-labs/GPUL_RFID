import sys

from MFRC522.MFRC522 import MFRC522
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

def init_gpio():
  GPIO.setwarnings(False) 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(GREEN_LED_PORT, GPIO.OUT)
  GPIO.output(GREEN_LED_PORT, False) 

def main():

  init_gpio()
  signal.signal(signal.SIGINT, end_read)
  continue_reading = True
  MIFAREReader = MFRC522()

  while continue_reading:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
      print "Card detected"
    #ENCENDER LEED
    (status,backData) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
      print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
      GPIO.output(GREEN_LED_PORT, True)
      print "encender led"
      #APAGAR LEED
    time.sleep(1)
    GPIO.output(GREEN_LED_PORT, False)

if __name__ == '__main__':
  main()
