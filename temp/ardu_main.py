# -*- coding:utf-8 -*-
import LED_display as LED
import threading
import keyboard
import time
import numpy as np
import random
import copy
import os
import sys
import serial 

ser = serial.Serial('/dev/ttyACM0', 9600)
ser_who = -1

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

SP= [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

A= [[0,1,0,0],
    [1,0,1,0],
    [1,1,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

B= [[1,1,0,0],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,1,0,0],
    [0,0,0,0]]

C= [[0,1,0,0],
    [1,0,1,0],
    [1,0,0,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,0,0,0]]

D= [[1,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,1,0,0],
    [0,0,0,0]]

E= [[1,1,1,0],
    [1,0,0,0],
    [1,1,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,0,0]]

F= [[1,1,1,0],
    [1,0,0,0],
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [0,0,0,0]]

G= [[0,1,1,0],
    [1,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]]

H= [[1,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

I= [[1,1,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [1,1,1,0],
    [0,0,0,0]]

J= [[0,0,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,0,0,0]]

K= [[1,0,1,0],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

L= [[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,0,0]]

M= [[1,0,1,0],
    [1,1,1,0],
    [1,1,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

N= [[0,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [1,0,1,0],
    [1,0,0,0],
    [0,0,0,0]]

O= [[0,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,0,0,0]]

P= [[1,1,0,0],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [0,0,0,0]]

Q= [[0,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,0,1,0]]

R= [[1,1,0,0],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

S= [[0,1,1,0],
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [1,1,0,0],
    [0,0,0,0]]

T= [[1,1,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,0,0,0]]

U= [[1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [0,0,0,0]]

V= [[1,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [0,1,0,0],
    [0,0,0,0]]

W= [[1,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [1,1,1,0],
    [1,0,1,0],
    [0,0,0,0]]

X= [[1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]]

Y= [[1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,0,0,0]]

Z= [[1,1,1,0],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,0,0]]

ex= [[0,1,0,0],
                [0,1,0,0],
                [0,1,0,0],
                [0,0,0,0],
                [0,1,0,0],
                [0,0,0,0]]
            
qst= [[1,1,0,0],
           [0,0,1,0],
           [0,1,0,0],
           [0,0,0,0],
           [0,1,0,0],
           [0,0,0,0]]

dot= [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,1,0,0],
      [0,0,0,0]]

hadot= [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,1,0,0],
          [1,0,0,0]]

colon= [[0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,1,0,0],
        [0,0,0,0]]

def write1(a,b):  # a는 글자 출력하고싶은 글자 리스트  , b는 컬러
        q=0
        for letter in a:
            for i in range(6):
                for j in range(4):
                    if letter[i][j]!=0:
                        LED.screen[i][j+q]=letter[i][j]+ b-1
            q+=4


def write2(a,b):
        q=0
        for letter in a:
            for i in range(6):
                for j in range(4):
                    if letter[i][j]!=0:
                        LED.screen[i+6][j+q]=letter[i][j]+b-1
            q+=4

def counting():
            write2([SP,SP,SP,num_3],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write2([SP,SP,SP,num_2],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]
            write2([SP,SP,SP,num_1],3)
            time.sleep(1)
            LED.screen = [[0 for x in range(32)] for x in range(16)]

iScreen = [[0 for x in range(32)] for x in range(16)]

#X = pygcurse.PygcurseWindow(32,16, fullscreen=False)

class Card:
    coord = None
    color = None
    count = None

    def __init__(self, coord = np.zeros((8,16)), color = 0, count = 0):
        # self.coord = np.zeros(shape=(8,16), dtype = int)
        self.coord = [  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.color = color +1 
        for i in range(8):
            for j in range(16):
                if coord[i][j] != 0:
                    self.coord[i][j] = coord[i][j] + color
                    #print(color)
        self.count = count

class Player:
    player_id = None
    time = None
    hand_cards = None 
    order = None
    card = None 
    live = None

    def __init__ (self, player_id = "", react = 0, hand_cards = [], order=0):
        self.player_id = player_id
        self.react = react
        self.hand_cards = hand_cards
        self.order = order
        self.card = None
        self.live = True

    def output(self):
        global present_surface_card, present_sum,present_total_card, time1

        if len(self.hand_cards) == 0:  
            lose()                  
        else:
            if self.card is not None:
                present_surface_card[0] = []
                present_sum[self.card.color-1] = present_sum[self.card.color-1] - self.card.count
            self.card = self.hand_cards.pop()
            present_surface_card[0] = [self.card]
            present_total_card = present_total_card+[self.card]
            present_sum[self.card.color-1] = present_sum[self.card.color-1] + self.card.count
            print("[R G Y B]")
            print(present_sum)
            if(self.order == 1):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i][j]=self.card.coord[i][j]
            elif(self.order == 2):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i][j+16]=self.card.coord[i][j]
            elif(self.order == 3):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j]=self.card.coord[i][j]
            elif(self.order == 4):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j+16]=self.card.coord[i][j]
            time1 = time.time() # card display time...

oneCard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

twoCard =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
            [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

threeCard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
             [1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1],
             [1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1],
             [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]] 

fourCard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1],
            [1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1],
            [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1],
            [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


fiveCard = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1],
            [1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1],
            [1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
            [1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

TAKE = 0
RING = 0
total_card = [] #리스트형의 전체 카드
present_sum = np.asarray([0,0,0,0]) # 각 카드에 대한 그림 개수 저장
present_surface_card = [[],[],[],[]]
present_total_card = [] # 필드에 있는 사용자들의 모든 카드
card1 = None
card2 = None
card3 = None
card4 = None
p1 = []
p2 = []
p3 = []
p4 = []
player_list=[]
who = -1
time1 = None

def LED_init():
    thread=threading.Thread(target=LED.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def initCard():
    global total_card
    for i in range(4):
        total_card.append(Card(oneCard, i, 1))
        total_card.append(Card(oneCard, i, 1))
        total_card.append(Card(oneCard, i, 1))
        total_card.append(Card(oneCard, i, 1))
        total_card.append(Card(oneCard, i, 1))
        total_card.append(Card(twoCard, i, 2))
        total_card.append(Card(twoCard, i, 2))
        total_card.append(Card(twoCard, i, 2))
        total_card.append(Card(threeCard, i, 3))
        total_card.append(Card(threeCard, i, 3))
        total_card.append(Card(threeCard, i, 3))
        total_card.append(Card(fourCard, i, 4))
        total_card.append(Card(fourCard, i, 4))
        total_card.append(Card(fiveCard, i, 5))
    random.shuffle(total_card)


def initPlayer():
    global total_card, p1,p2,p3,p4,player_list
    # getPlayerName() -> p1.name, p2.name, p3.name, p4.name 
    p1 = Player("P1", 0,total_card[0:14], 1)
    p2 = Player("P2", 0,total_card[14:28], 2)
    p3 = Player("P3", 0,total_card[28:42], 3)
    p4 = Player("P4", 0,total_card[42:], 4)
    player_list = [p1,p2,p3,p4]

def check_cards():
    global present_sum, TAKE
    # 检查在场牌数
    if 5 in present_sum:
        TAKE = 1  # 可拍铃
    else:
        TAKE = 0
    # print(present_sum,present_surface_card,RING,TAKE)


def update_label_remaining(): # LED 출력으로 바뀌어야 함
    global p1,p2,p3,p4,present_total_card,present_sum
    print("p1:",len(p1.hand_cards))
    print("p2:",len(p2.hand_cards))
    print("p3:",len(p3.hand_cards))
    print("p4:",len(p4.hand_cards))

########################################################################################
def gamesetlose():
    global p1,p2,p3,p4, player_list

    if len(p1.hand_cards) == 0 and p1.live == True:
        print("p1 lose")
        player_list.remove(p1)  
        for i in range(8):
            for j in range(16):

                LED.screen[i][j] = 0
        p1.live = False           
        p1.card = None     
 
    if len(p2.hand_cards) == 0 and p2.live == True:
        print("p2 lose")
        player_list.remove(p2)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j+16] = 0 
        p2.live = False       
        p2.card = None         

    if len(p3.hand_cards) == 0 and p3.live == True:
        print("p3 lose")
        player_list.remove(p3)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j] = 0 
        p3.live = False            
        p3.card = None    
 

    if len(p4.hand_cards) == 0 and p4.live == True:
        print("p4 lose")
        player_list.remove(p4)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16] = 0 
        p4.live = False    
        p4.card = None                
 
##################################################################

def write1(a,b):  # a는 글자 출력하고싶은 글자 리스트  , b는 컬러
        q=0
        for letter in a:
            for i in range(6):
                for j in range(4):
                    if letter[i][j]!=0:
                        LED.screen[i][j+q]=letter[i][j]+ b-1
            q+=4


def write2(a,b):
        q=0
        for letter in a:
            for i in range(6):
                for j in range(4):
                    if letter[i][j]!=0:
                        LED.screen[i+6][j+q]=letter[i][j]+b-1
            q+=4

def lose():
    global p1,p2,p3,p4, player_list

    if len(p1.hand_cards) == 0 and p1.live == True:
        print("p1 lose")
        player_list.remove(p1)  
        for i in range(8):
            for j in range(16):
                LED.screen[i][j] = 0
        p1.live = False           
        if(p1.card != None):
            present_sum[p1.card.color-1] = present_sum[p1.card.color-1] - p1.card.count
        p1.card = None     
 
    if len(p2.hand_cards) == 0 and p2.live == True:
        print("p2 lose")
        player_list.remove(p2)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j+16] = 0 
        p2.live = False  
        if (p2.card != None):     
            present_sum[p2.card.color-1] = present_sum[p2.card.color-1] - p2.card.count
        p2.card = None         

    if len(p3.hand_cards) == 0 and p3.live == True:
        print("p3 lose")
        player_list.remove(p3)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j] = 0 
        p3.live = False            
        if(p3.card != None):
            present_sum[p3.card.color-1] = present_sum[p3.card.color-1] - p3.card.count
        p3.card = None    
 

    if len(p4.hand_cards) == 0 and p4.live == True:
        print("p4 lose")
        player_list.remove(p4)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16] = 0 
        p4.live = False    
        if(p4.card != None):
            present_sum[p4.card.color-1] = present_sum[p4.card.color-1] - p4.card.count
        p4.card = None                
 

def consoleMatrix(screen):
    for i in screen:
        print(i)


def pygcurseMatrix(screen):
    for i in range(16):
        for j in range(32):
            if screen[i][j] == 1:
                win.putchar('@', j, i, 'red')
            elif screen[i][j] == 2:
                win.putchar('@', j, i, 'green')
            elif screen[i][j] == 3:
                win.putchar('@', j, i, 'blue')
            elif screen[i][j] == 4:
                win.putchar('@', j, i, 'yellow')    
            #default color = 'white', 'yellow' ,'fuchsia' ,'red', 'silver', 'gray', 'olive', 'purple', 'maroon', 'aqua', 'lime', 'teal', 'green', 'blue', 'navy', 'black'
    win.update()
flag=0
chk=0
def ser_input():
    global ser_who, time1
    ser_who = -1
    global flag
    while time.time() - time1 < 1 :
        if ser.readable():
            A=ser.readline()
            B=A.decode('utf8', 'ignore')[:len(A)-1].split()
            if(len(B) <4 ):
                continue
            if int(B[0])+int(B[1])+int(B[2])+int(B[3])<30:
                flag=0
            if int(B[0])> 100 and flag==0 and p1.live==True:
                if int(B[0])>750:
                    chk=1
                p1.time = time.time() - time1
                print(p1.time)
                ser_who = 1
                flag=1
                break
            if int(B[1])> 100 and flag==0 and p2.live==True:
                if int(B[1])>750:
                    chk=1
                p2.time = time.time() - time1
                print(p2.time)
                ser_who = 2
                flag=1
                break
            if int(B[2])> 100 and flag==0 and p3.live==True:
                if int(B[2])>750:
                    chk=1
                p3.time = time.time() - time1
                print(p3.time)
                ser_who = 3
                flag=1
                break
            if int(B[3])> 100 and flag==0 and p4.live==True:
                if int(B[3])>750:
                    chk=1
                p4.time = time.time() - time1
                print(p4.time)
                ser_who = 4
                flag=1
                break


def keyboard_input():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card, player_list
    global TAKE, RING, who, ser_who, chk
    
    #time1 = time.time()
    ser_input()
    if (ser_who == 1 and p1.live==True):
        if (TAKE == 1 and RING == 0):
            p1.hand_cards = present_total_card + p1.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None

            
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            write1([SP,P,num_1,SP,W,I,N,ex],5)
            time.sleep(1)
            counting()
            
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
          
            gamesetlose()
        elif TAKE == 0:
            if len(p1.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p1):
                        continue
                    player_list[i].hand_cards.insert(0, p1.hand_cards.pop())

                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                write1([SP,SP,P,num_1],5)
                write2([SP,W,R,O,N,G],5)
                time.sleep(3)
             
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0


            else:
                p1.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
        if p1.live==True:
            who = player_list.index(p1)
    elif (ser_who == 2 and p2.live==True):
        if (TAKE == 1 and RING == 0):
            p2.hand_cards = present_total_card + p2.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None

            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            write1([SP,P,num_2,SP,W,I,N,ex],5)
            time.sleep(3)
            
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0

            gamesetlose()
        elif TAKE == 0:
            if len(p2.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p2):
                        continue
                    player_list[i].hand_cards.insert(0, p2.hand_cards.pop())

                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                write1([SP,P,num_2,SP,N,O,P,E],5)
                time.sleep(3)
             
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
            else:
                p2.hand_cards = []
                lose()

        check_cards()
        update_label_remaining()
        if p2.live==True:
            who = player_list.index(p2)
    elif (ser_who == 3 and p3.live==True):
        if (TAKE == 1 and RING == 0):
            p3.hand_cards = present_total_card + p3.hand_cards

            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None

            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            write1([SP,P,num_3,SP,W,I,N,ex],5)
            time.sleep(3)
            
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            gamesetlose()
            # clean_cards()
        elif TAKE == 0:
            if len(p3.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p3):
                        continue
                    player_list[i].hand_cards.insert(0, p3.hand_cards.pop())
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                write1([SP,P,num_3,SP,N,O,P,E],5)
                time.sleep(3)
             
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
            else:
                p3.hand_cards = []
                lose()
  
        check_cards()
        update_label_remaining()
        if p3.live==True:
            who = player_list.index(p3)

    elif (ser_who == 4 and p4.live==True):
        if (TAKE == 1 and RING == 0):
            p4.hand_cards = present_total_card + p4.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None

            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            write1([SP,P,num_4,SP,W,I,N,ex],5)
            time.sleep(3)
            
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            # clean_cards()
            gamesetlose()
        elif TAKE == 0:
            if len(p4.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p4):
                        continue
                    player_list[i].hand_cards.insert(0, p4.hand_cards.pop())
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                write1([SP,P,num_4,SP,N,O,P,E],5)
                time.sleep(3)
             
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
            else:
                p4.hand_cards = []
                lose()

        check_cards()
        update_label_remaining()
        if p4.live==True:
            who = player_list.index(p4)
    elif ser_who == -1: 
        who = -1
    #elif ser_who==4 and p4.live==False:
     #   who= -1

    
p1_ready=0
p2_ready=0
p3_ready=0
p4_ready=0
a=0
b=0
def main():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE, who
    LED_init()
    initCard()
    initPlayer()

    global a
    global p1_ready
    global p2_ready
    global p3_ready
    global p4_ready
    global b

    ####################################### START READY ##############################################
    ####################################### END READY ##############################################
    LED.screen = [[0 for x in range(32)] for x in range(16)] # 게임 시작 전 LED CLEAR!
    who = 0                             # who: 누구차례인지 나타내는 변수, player_list의 index를 나타냄, 처음엔 index 0부터 시작
    while True: # 게임 while문
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            sys.exit()
        if(who != -1): i = who 
        player_list[i].output() 
        check_cards()                   # 5개짜리 있다면, TAKE =1 갱신
        # if(특정키 입력):
        #     update_label_remaining()  # 특정키 입력시 남은 카드 수 LED 출력 
        keyboard_input()          # 종친 플레이어의 index 반환
        if(who == -1):                  # 아무도 종을 안친 경우
            i = (i+1)%len(player_list)  # 다음 사람~
            if(i>len(player_list)):     # 플레이어 한명이 게임에서 진경우 player_list의 길이가 작아짐 그 경우 고려함
                i = i-1
        else:
            i = who                     # 누가 종친경우 그 사람의 index를 i로! 
            

if __name__ == '__main__':
    main()
