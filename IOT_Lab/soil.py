import RPi.GPIO as GPIO
import time

channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

try:
    while True:
        if not(GPIO.input(channel)):
            print("Water Detected!")
        else:
            print("No Water Detected!")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Exiting...")
    
finally:
    GPIO.cleanup()
