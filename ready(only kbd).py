import keyboard
import time




p1_ready=0
p2_ready=0
p3_ready=0
p4_ready=0
a=0
def player_ready():
    global a
    p1_ready=0
    p2_ready=0
    p3_ready=0
    p4_ready=0

    
    while True:
        
        if keyboard.is_pressed('1'):
            print("P1 Ready")
            p1_ready+=1
            time.sleep(1)
            for i in range(4):
                for j in range(8):
                    oScreen[i][j]=1
        if keyboard.is_pressed('2'):
            print("P2 Ready")
            p2_ready+=1
            time.sleep(1)
            for i in range(4):
                for j in range(8):
                    oScreen[i][j+8]=2

        if keyboard.is_pressed('3'):
            print("P3 Ready")
            p3_ready+=1
            time.sleep(1)
            for i in range(4):
                for j in range(8):
                    oScreen[i][j+16]=3
            
        if keyboard.is_pressed('4'):
            print("P4 Ready")
            p4_ready+=1
            time.sleep(1)
            for i in range(4):
                for j in range(8):
                    oScreen[i][j+24]=4
            
            
        if (p1_ready!=0 and p2_ready!=0) and (p3_ready!= 0 and p4_ready!= 0):
            print("all player get ready")
            a=1
            break
player_ready()
