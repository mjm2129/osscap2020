import LED_display as LED
import threading
import time
import random

card=[[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
       [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
       [1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1],
       [1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1],
       [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1],
       [1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1],
       [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1],
       [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

       [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1],
       [1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1],
       [1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
       [1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]]
       

def LED_init():
    thread=threading.Thread(target=LED.main, args=())
    thread.setDaemon(True)
    thread.start()
    return



LED_init()

while(1):
    for i in range(8):
        for j in range(16):
            LED.screen[i][j]=card[4][i][j]
    time.sleep(1)
    for i in range(8):
        for j in range(16):
            LED.screen[i][j]=card[0][i][j]
    time.sleep(1)