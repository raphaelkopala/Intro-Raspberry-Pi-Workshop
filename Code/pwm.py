import RPi.GPIO as GPIO
import atexit

ledPin = 19

def cleanup():
	GPIO.cleanup()

atexit.register(cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

pwmLed = GPIO.PWM(ledPin, 500)
pwmLed.start(100)


while (True):
	input = raw_input("Enter brightness (0-100):")
	duty = int(input)
	if (duty>=0 and duty<=100):
		pwmLed.ChangeDutyCycle(duty)
	else:
		print "Try Again"
 



