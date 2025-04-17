from gpiozero import InputDevice
import time
no_rain = InputDevice(4)

while True:
    if not no_rain.is_active:
        print("Raining ...")
    else:
        print("No rain")  # Placeholder for 'Not Raining'
    time.sleep(0.5)
