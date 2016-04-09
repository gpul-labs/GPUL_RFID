import sys

sys.path.append('/MFRC522')
import MFRC522
import signal
import time

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

cardA = [5,74,28,185,234]
cardB = [83,164,247,164,164]
cardC = [20,38,121,207,132]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()


def main():
  sys.path.append('/MFRC522')
  signal.signal(signal.SIGINT, end_read)

  while continue_reading:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
      print "Card detected"
    #ENCENDER LEED
    (status,backData) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
      print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    #APAGAR LEED
    time.sleep(1)

if __name__ == '__main__':
  main()