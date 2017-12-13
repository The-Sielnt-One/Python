import time
import RPi.GPIO as GPIO
#from inter import fr
    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT) #trigger
GPIO.setup(24,GPIO.IN) #echo

#def marche(ch): ##here
    #if (ch=='A'):
    #elif (ch=='B'):
    #elif (ch=='R'):
    #elif (ch=='amphi'):

def frust():
    turnL(17,18,22,23)
    time.sleep(1)
    turnR(17,18,22,23)
    
def mav(t):
    GPIO.output(t[0],True)
    GPIO.output(t[1],False)
    GPIO.output(t[2],True)
    GPIO.output(t[3],False)
    time.sleep(1)
def mac(x1,y1,t,c=0):
    i=capt(x1,y1)
    if (c==5):
        #fr()
        return 0
    if (i>25): 
        mav(t)
        return 1
    else:
        stp(t[0],t[1],t[2],t[3])
        time.sleep(2)
        mac(x1,y1,t,c+1)
        
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

def capt(x1,y1):
    GPIO.output(x1,False)
    time.sleep(1)
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
    return d
        #ex=mav(t[0],t[1],t[2],t[3],d)
        #if (ex==0):
            #mar(t[0],t[1],t[2],t[3]) ##here
        #time.sleep(0.1)
mav((17,18,22,23))
stp(17,18,22,23)
mar(17,18,22,23)
#mav(16,24,(17,18,22,23))
stp(17,18,22,23)
turnL(17,18,22,23)
stp(17,18,22,23)
turnR(17,18,22,23)
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