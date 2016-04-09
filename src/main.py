import sys

from MFRC522.MFRC522 import MFRC522
import signal
import time

import RPi.GPIO as GPIO

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  #MIFAREReader.GPIO_CLEAN()
  GPIO.cleanup()

def main():

  GPIO.setwarnings(False) 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11, GPIO.OUT)
  GPIO.output(11, False) 
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
      GPIO.output(11, True)
      print "encender led"
      #APAGAR LEED
    time.sleep(1)
    GPIO.output(11, False)

if __name__ == '__main__':
  main()
