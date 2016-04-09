import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time lry


class ProxSensor(object):
  
  def __init__(self):                     #Set GPIO pin numbering 
    self.TRIG = 16                                  #Associate pin 23 to TRIG
    self.ECHO = 18
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(self.ECHO,GPIO.IN) 
    
  def medir(self):                         #Associate pin 24 to ECH                           #Delay of 2 seconds

    GPIO.output(self.TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(self.TRIG, False)                 #Set TRIG as LOW
    pulse_start=0
    pulse_end=0
    while GPIO.input(self.ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(self.ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    return round(distance, 2)            #Round to two decimal points

def main():
  proxSensor = ProxSensor()
  while True:
    time.sleep(1)
    print proxSensor.medir()

if __name__ == '__main__':
  main()
