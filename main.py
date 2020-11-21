import LED_display as LED
import threading
import time


def LED_init():
    thread=threading.Thread(target=LED.main, args=())
    thread.setDaemon(True)
    thread.start()
    return



LED_init()

while(1):
    LED.fill_rectangle(0,0,16,1,1)
    LED.fill_rectangle(0,7,16,8,1)
    LED.fill_rectangle(0,0,1,8,1)
    LED.fill_rectangle(15,0,16,8,1)
    time.sleep(1)
    LED.fill_rectangle(7,3,9,5,1)
