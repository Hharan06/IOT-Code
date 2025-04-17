import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
pin_1 = 17  
pin_2 = 27  
GPIO.setup(pin_1, GPIO.OUT)
GPIO.setup(pin_2, GPIO.OUT)

try:
    while True:
        
        GPIO.output(pin_1, GPIO.LOW)
        GPIO.output(pin_2, GPIO.HIGH)
        time.sleep(0.5)          
        GPIO.output(pin_1, GPIO.HIGH)
        GPIO.output(pin_2, GPIO.LOW)
        
        time.sleep(0.1)
        GPIO.output(pin_1, GPIO.LOW)
        GPIO.output(pin_2, GPIO.HIGH)
        GPIO.output(pin_1, GPIO.HIGH)
        GPIO.output(pin_2, GPIO.LOW)
        
        time.sleep(0.5)
        GPIO.output(pin_1, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(pin_1, GPIO.HIGH)        
        time.sleep(0.1)
        GPIO.output(pin_1, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(pin_1, GPIO.HIGH)        
        time.sleep(0.1)
        
        GPIO.output(pin_1, GPIO.LOW)
        GPIO.output(pin_1, GPIO.HIGH)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()