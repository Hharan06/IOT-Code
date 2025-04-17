import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 23  # Trigger Pin
ECHO = 24  # Echo Pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send 10µs pulse to trigger pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG, False)

    # Record the time for the echo signal
    start_time = time.time()
    stop_time = time.time()

    # Wait for the echo pin to go HIGH
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for the echo pin to go LOW
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Time difference between sending and receiving pulse
    time_elapsed = stop_time - start_time

    # Speed of sound is 34300 cm/s, calculate distance
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
