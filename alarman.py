import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1,out1 = 36,38
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(in1,GPIO.IN)

while True:
    sensor=GPIO.input(36)
    print(sensor)
    if(sensor==1):
        GPIO.output(out1,GPIO.HIGH)
        time.sleep(5)
    else:
        GPIO.output(out1,GPIO.LOW)
        
GPIO.cleanup()
