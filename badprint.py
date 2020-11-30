num_1=[[0,1,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,0,0],
       [1,1,1,0],
       [0,0,0,0]]

num_2=[[0,1,0,0],
       [1,0,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [1,1,1,0],
       [0,0,0,0]]

num_3=[[1,1,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]]

num_4=[[1,0,1,0],
       [1,0,1,0],
       [1,1,1,0],
       [0,0,1,0],
       [0,0,1,0],
       [0,0,0,0]]

num_5=[[1,1,1,0],
       [1,0,0,0],
       [1,1,0,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]]

num_6=[[0,1,1,0],
       [1,0,0,0],
       [1,1,0,0],
       [1,0,1,0],
       [0,1,0,0],
       [0,0,0,0]]

num_7=[[1,1,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [1,0,0,0],
       [1,0,0,0],
       [0,0,0,0]]

num_8=[[0,1,1,0],
       [1,0,1,0],
       [0,1,0,0],
       [1,0,1,0],
       [1,1,0,0],
       [0,0,0,0]]

num_9=[[0,1,0,0],
       [1,0,1,0],
       [0,1,1,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]]

num_0=[[0,1,0,0],
       [1,0,1,0],
       [1,1,1,0],
       [1,0,1,0],
       [0,1,0,0],
       [0,0,0,0]]





list=[[[0,1,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,0,0],
       [1,1,1,0],
       [0,0,0,0]],

        [[0,1,0,0],
       [1,0,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [1,1,1,0],
       [0,0,0,0]],

[[1,1,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]],

[[1,0,1,0],
       [1,0,1,0],
       [1,1,1,0],
       [0,0,1,0],
       [0,0,1,0],
       [0,0,0,0]],

[[1,1,1,0],
       [1,0,0,0],
       [1,1,0,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]],

[[0,1,1,0],
       [1,0,0,0],
       [1,1,0,0],
       [1,0,1,0],
       [0,1,0,0],
       [0,0,0,0]],

[[1,1,1,0],
       [0,0,1,0],
       [0,1,0,0],
       [1,0,0,0],
       [1,0,0,0],
       [0,0,0,0]],

[[0,1,1,0],
       [1,0,1,0],
       [0,1,0,0],
       [1,0,1,0],
       [1,1,0,0],
       [0,0,0,0]],

[[0,1,0,0],
       [1,0,1,0],
       [0,1,1,0],
       [0,0,1,0],
       [1,1,0,0],
       [0,0,0,0]],

[[0,1,0,0],
       [1,0,1,0],
       [1,1,1,0],
       [1,0,1,0],
       [0,1,0,0],
       [0,0,0,0]]]
aaa=[]
'''
def printtime(a):
    aaa=[]
    a=str(a)
    for j in range(5):
        for i in ['1','2','3','4','5','6','7','8','9','0']:
            if i==a[j]:
                if a[j]=='1':
                    aaa.append(num_1)
                if a[j]=='2':
                    aaa.append(num_2)
                if a[j]=='3':
                    aaa.append(num_3)
                if a[j]=='4':
                    aaa.append(num_4)
                if a[j]=='5':
                    aaa.append(num_5)
                if a[j]=='6':
                    aaa.append(num_6)
                if a[j]=='7':
                    aaa.append(num_7)
                if a[j]=='8':
                    aaa.append(num_8)
                if a[j]=='9':
                    aaa.append(num_9)
                if a[j]=='0':
                    aaa.append(num_0)



    print(aaa[0])
    print(aaa[1])'''


def printgoodgameset(a,p_time):
    
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                        
                aaa=[]
                a=str(p_time)
                for j in range(5):  
                    for i,p in zip(['1','2','3','4','5','6','7','8','9','0'],[num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_0]):
                        if i==a[j]:
                            aaa.append(p)
                            
                write1([SP,P,a,SP,W,I,N,ex],5)
                write2(aaa,5)

                time.sleep(2)
                
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0

                for i in [num_3,num_2,num_1]:
                    write0([SP,SP,SP,i],3)
                    time.sleep(1)
                    clean2()

                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0


a=14
b=12
c=10
d=55



def clean3():
    for i in range(6,13,1):
        for j in range(15,19,1):
            LED.screen[i][j]=0
            
def writecal(a,b,c,d):
    q=0
    for letter in a:
        for i in range(6):
            for j in range(4):
                if letter[i][j]!=0:
                     LED.screen[i+c][j+d]=letter[i][j]+b-1
        q+=4
    
def printbadgameset(a,p1_len,p2_len,p3_len,p4_len):
    for i in range(16):
        for j in range(32):
             LED.screen[i][j]=0

    p1_len=str(p1_len)
    p2_len=str(p2_len)
    p3_len=str(p3_len)
    p4_len=str(p4_len)
    ccc=[]
    for u in [p1_len, p2_len, p3_len, p4_len]:
        bbb=[]
        for j in range(len(u)):  
            for i,p in zip(['1','2','3','4','5','6','7','8','9','0'],[num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_0]):
                if i==u[j]:
                    bbb.append(p)
        ccc.append(bbb)

    writecal(ccc[0],7,0,0)
    writecal(ccc[1],7,24,0)
    writecal(ccc[2],7,0,10)
    writecal(ccc[3],7,24,10)
    
    for i in [num_3,num_2,num_1]:
        write0([SP,SP,SP,i],3)
        time.sleep(1)
        clean3()

    
    for i in range(16):
        for j in range(32):
            LED.screen[i][j]=0

