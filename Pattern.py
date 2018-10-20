import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

n=10
for i in range(n):
    GPIO.output(37,True)
    GPIO.output(35,True)
    GPIO.output(33,True)
    GPIO.output(31,True)
    time.sleep(1)
    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,False)
    GPIO.output(31,False)            
    time.sleep(1)

for i in range(n):
    GPIO.output(37,True)
    GPIO.output(35,False)
    GPIO.output(33,False)
    GPIO.output(31,False)
    time.sleep(1)
    
    GPIO.output(37,False)
    GPIO.output(35,True)
    GPIO.output(33,False)
    GPIO.output(31,False)            
    time.sleep(1)

    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,True)
    GPIO.output(31,False)            
    time.sleep(1)

    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,False)
    GPIO.output(31,True)            
    time.sleep(1)



for i in range(n):
    GPIO.output(37,True)
    GPIO.output(35,True)
    GPIO.output(33,False)
    GPIO.output(31,False)
    time.sleep(1)
    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,True)
    GPIO.output(31,True)            
    time.sleep(1)
    
for i in range(n):
    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,False)
    GPIO.output(31,True)
    time.sleep(1)
    
    GPIO.output(37,False)
    GPIO.output(35,False)
    GPIO.output(33,True)
    GPIO.output(31,False)            
    time.sleep(1)
    
    GPIO.output(37,False)
    GPIO.output(35,True)
    GPIO.output(33,False)
    GPIO.output(31,False)            
    time.sleep(1)
    
    GPIO.output(37,True)
    GPIO.output(35,False)
    GPIO.output(33,False)
    GPIO.output(31,True)            
    time.sleep(1)
print("Done")
GPIO.cleanup()
    
