mport RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

Lred =  13
Lblue = 15
PIR = 11

GPIO.setup(Lred, GPIO.OUT)
GPIO.setup(Lblue, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)
while True:
        i=GPIO.input(PIR)
        if i==0:
            print("¡Sin movimiento!", i )
            GPIO.output(Lred,False)
            GPIO.output(Lblue,True)
            time.sleep(2)
        elif i==1:
            print("¡Detección de movimiento!", i)
            GPIO.output(Lred,True)
            GPIO.output(Lblue,False)
            time.sleep(2)
            GPIO.output(Lred,False)
            time.sleep(3)
