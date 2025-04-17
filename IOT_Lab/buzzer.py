import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 18  
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def buzz(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:  
        buzz(BUZZER_PIN, 0.5)
        time.sleep(1.5)

except KeyboardInterrupt:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.cleanup()
