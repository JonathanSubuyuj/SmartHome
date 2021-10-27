import RPi.GPIO as GPIO          
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Ena,in1,in2,a,c,p = 3,5,7,8,10,40
GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(p,GPIO.OUT)
pwm = GPIO.PWM(Ena,100)
pwm.start(0)

while True:
  
    button1=GPIO.input(a)
    button2=GPIO.input(c)
    button3=GPIO.input(p)
    print(button1)
    print(button2)
    print(button3)
    
    if (button3==1):
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

    elif (button1==1):
        print ("abrir")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        pwm.ChangeDutyCycle(14)
        time.sleep(0.2)
        
    elif (button2==1):
        print ("Cerrar")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        pwm.ChangeDutyCycle(4)
        time.sleep(0.2)
    
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

pwm.stop()
GPIO.cleanup()
    
  