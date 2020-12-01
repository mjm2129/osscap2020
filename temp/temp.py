
    while True:
        if keyboard.is_pressed('s'):
            write1([P,R,E,S,S,],2)
            write2([T,O,SP,S,T,A,R,T],3)
            time.sleep(1)
            b+=1
            break
            
    while b!=0:
        time.sleep(0.08)
        if keyboard.is_pressed('1'):
            p1_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i+12][j]=1
        if keyboard.is_pressed('2'):
            p2_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i+12][j+8]=2

        if keyboard.is_pressed('3'):
            p3_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i+12][j+16]=3
            
        if keyboard.is_pressed('4'):
            p4_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i+12][j+24]=4

            
        
        if (p1_ready!=0 and p2_ready!=0) and (p3_ready!= 0 and p4_ready!= 0):
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)] 
            print("all player get ready")
            time.sleep(1)
            write1([A,L,L,P,L,A,Y,E],3)
            write2([R,E,A,D,Y,ex],4)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write1([G,A,M,E],3)
            write2([S,T,A,R,T,ex],4)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            
            
            write1([SP,SP,num_5],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write1([SP,SP,num_4],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write1([SP,SP,num_3],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write1([SP,SP,num_2],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write1([SP,SP,num_1],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
                    
            a=1
            break

