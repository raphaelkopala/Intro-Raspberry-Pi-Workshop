

from Tkinter import *
import RPi.GPIO as GPIO
import atexit
import tkMessageBox

ledPin = 19
buttonPin = 23
storedPwm = 0

def cleanup():
	GPIO.cleanup()
	win.destroy()

def update(duty):
	pwm_led.ChangeDutyCycle(int(duty))

def toggle():
        if scale.get() > 0:
                global storedPwm
                storedPwm= scale.get()
                scale.set(0)
                pwm_led.ChangeDutyCycle(0)
        else:
                pwm_led.ChangeDutyCycle(int(storedPwm))
                scale.set(storedPwm)

def task():
        win.update()
        if GPIO.input(buttonPin):
                tkMessageBox.showwarning("Warning!","Button Hit!")

atexit.register(cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm_led = GPIO.PWM(ledPin, 500)
pwm_led.start(100)

win = Tk()

win.title("LED PWM Switch")
win.geometry("500x100")
win.protocol("WM_DELETE_WINDOW", cleanup)

scale = Scale(win, from_=0, to= 100, orient=HORIZONTAL, length = 400, tickinterval=10, command=update)
scale.pack()
scale.set(100)

toggleButton = Button(win, text="Toggle", command=toggle)
toggleButton.pack()

while 1:
        task()





