import RPi.GPIO as GPIO
import time
import atexit

ledPin = 19

def cleanup():
	GPIO.cleanup()

atexit.register(cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

while (True):
	GPIO.output(ledPin,True)
	time.sleep(0.5)
	GPIO.output(ledPin,False)
	time.sleep(0.5)
