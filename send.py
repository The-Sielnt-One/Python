import SendKeys
import time
import os
def Text():
    os.startfile('exp.txt')
    msg='Fuck you , you piece of shit+.'
    time.sleep(2)
    SendKeys.SendKeys(msg,with_spaces=True,pause=0.01)
Text()
