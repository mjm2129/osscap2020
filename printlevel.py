def writecal1(a,b,c,d):
    q=0
    for letter in a:
        for i in range(5):
            for j in range(4):
                if letter[i][j]!=0:
                     LED.screen[i+c][j+d+q]=letter[i][j]+b-1
        q+=4

wrical1([num_1,dot,H,A,R,D],1,0,0)
wrical1([num_2,dot,N,O,R,M,A,L],2,6,0)
wrical1([num_3,dot,E,A,S,Y],3,12,0)
