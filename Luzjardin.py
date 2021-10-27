import RPi.GPIO as GPIO                    
import time                                
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 29                                  
ECHO = 31                                  
ot1 = 12

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(ot1,GPIO.OUT)

try:
    while True:
        GPIO.output(TRIG, False)                   
        time.sleep(2)
        GPIO.output(TRIG, True)                    
        time.sleep(0.00001)                        
        GPIO.output(TRIG, False)                      
        
        while GPIO.input(ECHO)==0:                 
            pulse_start = time.time()             

        while GPIO.input(ECHO)==1:                 
            pulse_end = time.time()  
         
        t = pulse_end - pulse_start               

        distancia = t*17150                     
        distancia = round(distancia, 2)            
        print(distancia)
        
    if (distancia < 5):      
        GPIO.output(ot1,True)
    
     else:
        GPIO.output(ot1,False)