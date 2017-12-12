import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT) #trigger
GPIO.setup(24,GPIO.IN) #echo

def marche(ch):
    if (ch=='A'):
    elif (ch=='B'):
    elif (ch=='R'):
    elif (ch=='amphi'):

def mav(x1,y1,x2,y2,i,c=0):
    if (c==5):
        
    if (i>25): 
        GPIO.output(x1,True)
        GPIO.output(y1,False)
        GPIO.output(x2,True)
        GPIO.output(y2,False)
        time.sleep(0.1)
    else:
        stp(x1,y1,x2,y2)
        time.sleep(5)
        mav(x1,y1,x2,y2,i,c+1)
        
def mar(x1,y1,x2,y2):
    GPIO.output(x1, False)
    GPIO.output(y1, True)
    GPIO.output(x2, False)
    GPIO.output(y2, True)
    time.sleep(1)

def stp(x1,y1,x2,y2):
    GPIO.output(x1, False)
    GPIO.output(y1, False)
    GPIO.output(x2, False)
    GPIO.output(y2, False)
    time.sleep(1)

def turnR(x1,y1,x2,y2):
    GPIO.output(x1,0)
    GPIO.output(y1,1)
    GPIO.output(x2,1)
    GPIO.output(y2,0)
    time.sleep(0.5)
    
def turnL(x1,y1,x2,y2):
    GPIO.output(x1,1)
    GPIO.output(y1,0)
    GPIO.output(x2,0)
    GPIO.output(y2,1)
    time.sleep(0.5)

def capt(x1,y1,v,t):
    GPIO.output(x1,False)
    time.sleep(1)
    for i in range(v):
        GPIO.output(x1,True)
        time.sleep(0.00001)
        GPIO.output(x1,False)
        while GPIO.input(y1)==0:
            start=time.time()
        while GPIO.input(y1)==1:
            end=time.time()
        dur=end - start
        d=(331/2)*dur*100
        print (d)
        mav(t[0],t[1],t[2],t[3],d)
        time.sleep(0.1)

#def Advance(x1,y1,n,t):
    #i=0
    #while True :
        #d=capt(x1,y1,1,t)
        #if (d>20):
            #GPIO.output(t[0],1)
            #GPIO.output(t[1],0)
            #GPIO.output(t[2],1)
            #GPIO.output(t[3],0)
            #time.sleep(0.1)
            #i+=1
        #else:
            #GPIO.output(t[0],0)
            #GPIO.output(t[1],0)
            #GPIO.output(t[2],0)
            #GPIO.output(t[3],0)
            #time.sleep(5)  
        #if (i == n-1):
            #GPIO.output(t[0],0)
            #GPIO.output(t[1],0)
            #GPIO.output(t[2],0)
            #GPIO.output(t[3],0)
            #time.sleep(0.5)
            #break 
    
GPIO.cleanup()