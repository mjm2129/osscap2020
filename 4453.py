
def timemoveprint(a):
        eee=[]
        for tlrks in a:
            ddd=[]
            for j in range(8):  
                for i,p in zip([' ','P','1','2','3','4','5','6','7','8','9','0','.'],[SP,P,num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_0,dot]):
                    if i==tlrks[j]:
                        ddd.append(p)
            eee.append(ddd)
    
        creditlist=[[0 for x in range(32)] for x in range(60)]
        
        
     
        i=0
        j=0
        for plandtime in eee:
            for letter in plandtime:
                #print(letter)
                for spzks in letter:
                    #print(spzks)
                    for gkszks in spzks:
                        creditlist[i][j]=gkszks
                        j+=1
                    i+=1
                    j-=4
                i-=6
                j+=4
            i+=6
            j-=32
        for p in range(60):
            for j in range(32):
                LED.screen[15][j]=creditlist[p][j]
            pygcurseMatrix(oScreen)
            time.sleep(0.15)
            for a in range(15):
                for b in range(32):
                    LED.screen[a][b]=LED.screen[a+1][b]
                    LED.screen[a+1][b]=0


   

    timemoveprint(a)
