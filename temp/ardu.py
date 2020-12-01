import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    if ser.readable():
        A=ser.readline()
        B=A.decode('utf8', 'ignore')[:len(A)-1].split()
        if(len(B) <4 ):
            continue
        if(int(B[0]) + int(B[1]) + int(B[2]) + int(B[3])) > 10:
            print(B)
