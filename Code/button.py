import RPi.GPIO as GPIO
import atexit

ledPin = 19
buttonPin = 23

def cleanup():
	GPIO.cleanup()

atexit.register(cleanup)

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT)

lastState = False

while (True):
	currentState=GPIO.input(buttonPin)
	if lastState != currentState:
		GPIO.output(ledPin,currentState)
		print(currentState)
		lastState = currentState

		
