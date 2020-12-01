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
       [1,0,1,0],
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
def clean1():
    for i in range(8):
        for j in range(32):
            LED.screen[i][j]=0

def clean2():
    for i in range(6,16,1):
        for j in range(32):
            LED.screen[i][j]=0

def clean3():
    for i in range(1,13,1):
        for j in range(14,19,1):
            LED.screen[i][j]=0

def write0(a,b):  
        q=0
        for letter in a:
            for i in range(6):
                for j in range(4):
                    if letter[i][j]!=0:
                        LED.screen[i+6][j+q+2]=letter[i][j]+ b-1
            q+=4

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

def printgoodgameset(a,p_time,p1_len, p2_len, p3_len, p4_len): 
                global calm
                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0
                p_time = str(p_time)
                aaa = []
                for j in range(len(p_time)):  
                    for i,p in zip(['1','2','3','4','5','6','7','8','9','0'],[num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_0]):
                        if i==p_time[j]:
                            aaa.append(p)
                aaa.insert(0,SP)
                aaa.insert(0,SP)
                aaa.insert(3,dot)
                write1([SP,P,a,SP,W,I,N,ex],6)
                write2(aaa,6)
                time.sleep(2.5)

                if calm == True:
                    for i in range(16):
                        for j in range(32):
                            LED.screen[i][j]=0
                    write1([SP,SP,C,A,L,M], 7)
                    write2([SP,SP,D,O,W,N,ex], 7)
                    time.sleep(1)

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
                writecal(ccc[1],7,0,24)
                writecal(ccc[2],7,10,0)
                writecal(ccc[3],7,10,24)
              

                for i in [num_3,num_2,num_1]:
                    write0([SP,SP,SP,i],3)
                    time.sleep(1)
                    clean3()

                for i in range(16):
                    for j in range(32):
                        LED.screen[i][j]=0

            
def writecal(a,b,c,d):
    q=0
    for letter in a:
        for i in range(6):
            for j in range(4):
                if letter[i][j]!=0:
                     LED.screen[i+c][j+d+q]=letter[i][j]+b-1
        q+=4
    
def printbadgameset(a,p1_len,p2_len,p3_len,p4_len):
    temp_screen = [[0 for x in range(32)] for x in range(16)]
    for i in range(16):
        for j in range(32):
            temp_screen[i][j]= LED.screen[i][j]

    for i in range(16):
        for j in range(32):
            LED.screen[i][j]=0
    write1([SP,P,a,SP,F,A,I,L],1)
    time.sleep(1.5)
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
    writecal(ccc[1],7,0,24)
    writecal(ccc[2],7,10,0)
    writecal(ccc[3],7,10,24)
    
    for i in [num_3,num_2,num_1]:
        write0([SP,SP,SP,i],3)
        time.sleep(1)
        clean3()

    
    for i in range(16):
        for j in range(32):
            LED.screen[i][j] = temp_screen[i][j] 


class Card:
    coord = None
    color = None
    count = None

    def __init__(self, coord = np.zeros((8,16)), color = 0, count = 0):

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

        self.count = count

class Player:
    player_id = None
    time = 9.9
    hand_cards = None 
    order = None
    card = None 
    live = None

    def __init__ (self, player_id = "", time = 0, hand_cards = [], order=0):
        self.player_id = player_id
        self.time = time
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
            time1 = time.time()

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

def finish_print():
    write

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
    p1 = Player("P1", 9.99,total_card[0:14], 1)
    p2 = Player("P2", 9.99,total_card[14:28], 2)
    p3 = Player("P3", 9.99,total_card[28:42], 3)
    p4 = Player("P4", 9.99,total_card[42:], 4)
    player_list = [p1,p2,p3,p4]

def check_cards():
    global present_sum, TAKE
    if 5 in present_sum:
        TAKE = 1  
    else:
        TAKE = 0


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



def lose():
    global p1,p2,p3,p4, player_list

    if len(p1.hand_cards) == 0 and p1.live == True:
        print("p1 lose")
        player_list.remove(p1) 
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            react()
            sys.exit()
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
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            react()
            sys.exit()
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
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            react()
            sys.exit()
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
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            react()
            sys.exit()
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16] = 0 
        p4.live = False    
        if(p4.card != None):
            present_sum[p4.card.color-1] = present_sum[p4.card.color-1] - p4.card.count
        p4.card = None                
 

flag=0
flag_1 = 0
flag_2 = 0
flag_3 = 0
flag_4 = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
p1_ready = p2_ready = p3_ready = p4_ready = False
calm = False

def ser_input():
    global ser_who, time1, t1, t2, t3, t4, check, ready_state, p1_ready, p2_ready, p3_ready, p4_ready
    ser_who = -1
    global flag, flag1, flag2, flag3, flag4, calm
    if ready_state == False:
        t=9999
    else:
        t=1
    while time.time() - time1 < t :
        if ser.readable():
            read = ser.readline()
            read2 = read.decode('utf8', 'ignore')[:len(read)-1].split()
            if(len(read2) < 4):
                continue
            if ready_state == False:
                if int(read2[0]) > 30:
                    p1_ready = True
                    for i in range(4):
                        for j in range(8):
                            LED.screen[i+12][j]=1
                if int(read2[1]) > 30:
                    p2_ready = True
                    for i in range(4):
                        for j in range(8):
                            LED.screen[i+12][j+8]=2
                if int(read2[2]) > 30:
                    p3_ready = True
                    for i in range(4):
                        for j in range(8):
                            LED.screen[i+12][j+16]=3
                if int(read2[3]) > 30:
                    p4_ready = True
                    for i in range(4):
                        for j in range(8):
                            LED.screen[i+12][j+24]=4

                if(p1_ready == True and p2_ready == True and p3_ready == True and p4_ready == True):
                    flag=1
                    ready_state=True
                    return 
            else:
                calm = False
                if int(read2[0])+int(read2[1])+int(read2[2])+int(read2[3])<30:
                    flag=0
                if int(read2[0])> 150 and flag==0 and p1.live==True:
                    print(read2[0])
                    if int(read2[0])>400:
                        calm = True
                    t1 = time.time() - time1
                    ser_who = 1
                    flag=1
                    break
                if int(read2[1])> 150 and flag==0 and p2.live==True:
                    print(read2[1])
                    if int(read2[1])>400:
                        calm = True
                    t2 = time.time() - time1
                    ser_who = 2
                    flag=1
                    break
                if int(read2[2])> 150 and flag==0 and p3.live==True:
                    print(read2[2])
                    if int(read2[2])>400:
                        calm = True
                    t3 = time.time() - time1
                    ser_who = 3
                    flag=1
                    break
                if int(read2[3])> 150 and flag==0 and p4.live==True:
                    print(read2[3])
                    if int(read2[3])>400:
                        calm = True
                    t4 = time.time() - time1
                    ser_who = 4
                    flag=1
                    break
    
 
def keyboard_input():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card, player_list
    global TAKE, who, ser_who, time1, t1, t2, t3, t4
    
    #time1 = time.time()
    ser_input()
    if (ser_who == 1 and p1.live==True):
        if (TAKE == 1):
            p1.time = round(min(float(t1), p1.time),3)
            print(p1.time)
            p1.hand_cards = present_total_card + p1.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None
            t1 = round(t1,3)
            printgoodgameset(num_1,t1 , len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            gamesetlose()
        elif TAKE == 0:
            if len(p1.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p1):
                        continue
                    player_list[i].hand_cards.insert(0, p1.hand_cards.pop())
                printbadgameset(num_1, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            else:
                p1.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
        if p1.live==True:
            who = player_list.index(p1)
    elif (ser_who == 2 and p2.live==True):
        if (TAKE == 1):
            p2.time = round(min(float(t2),p2.time),3)
            print(p2.time)
            p2.hand_cards = present_total_card + p2.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None
            t2 = round(t2,3)
            printgoodgameset(num_2, t2, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            gamesetlose()
        elif TAKE == 0:
            if len(p2.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p2):
                        continue
                    player_list[i].hand_cards.insert(0, p2.hand_cards.pop())

                printbadgameset(num_2, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            else:
                p2.hand_cards = []
                lose()

        check_cards()
        update_label_remaining()
        if p2.live==True:
            who = player_list.index(p2)
    elif (ser_who == 3 and p3.live==True):
        if (TAKE == 1):
            p3.time = round(min(p3.time,float(t3)) ,3)
            print(p3.time)
            p3.hand_cards = present_total_card + p3.hand_cards

            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None
            t3 = round(t3,3)
            printgoodgameset(num_3, t3, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            gamesetlose()
            # clean_cards()
        elif TAKE == 0:
            if len(p3.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p3):
                        continue
                    player_list[i].hand_cards.insert(0, p3.hand_cards.pop())
                printbadgameset(num_3, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            else:
                p3.hand_cards = []
                lose()
  
        check_cards()
        update_label_remaining()
        if p3.live==True:
            who = player_list.index(p3)

    elif (ser_who == 4 and p4.live==True):
        if (TAKE == 1):
            p4.time = round(min(float(t4),p4.time), 3)
            print(p4.time)
            p4.hand_cards = present_total_card + p4.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            TAKE = 0
            if(len(p1.hand_cards) != 0): p1.card = None
            if(len(p2.hand_cards) != 0): p2.card = None
            if(len(p3.hand_cards) != 0): p3.card = None
            if(len(p4.hand_cards) != 0): p4.card = None
            t4 = round(t4,3)
            printgoodgameset(num_4, t4, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
            gamesetlose()
        elif TAKE == 0:
            if len(p4.hand_cards) > len(player_list)-1:
                for i in range(len(player_list)):
                    if i == player_list.index(p4):
                        continue
                    player_list[i].hand_cards.insert(0, p4.hand_cards.pop())
                printbadgameset(num_4, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
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


React=[]
file_line=[]

def react():
    global p1,p2,p3,p4
    global React, file_line
    text_file = open("test.txt", "r")
    file_line=text_file.readlines()
    React.append(p1.time)
    React.append(p2.time)
    React.append(p3.time)
    React.append(p4.time)
    txt_line=file_line
    for i in range(4):
        for j in range(10):
            if file_line[j][0]!='P':
                continue
            elif React[i]<float(file_line[j][3:8]):
                txt_line.insert(j,'P'+str(i+1)+' '+str(React[i])+'\n')
                del file_line[10]
                break
    win_player = player_list.pop()
    for i in range(16):
        for j in range(32):
            LED.screen[i][j] = 0 
    char = win_player.player_id[1]
    print(char,"win")
    print(type(char))
    if(char == '1') : write1([P,num_1,SP,W,I,N,ex],7)
    if(char == '2') : write1([P,num_2,SP,W,I,N,ex],7)
    if(char == '3') : write1([P,num_3,SP,W,I,N,ex],7)
    if(char == '4') : write1([P,num_4,SP,W,I,N,ex],7)
    time.sleep(2)
    text_file = open("test.txt", "w")
    for i in range(10):
        data=txt_line[i]
        text_file.write(data)
    React=[]
    
def main():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE, who, ready_state, time1
    LED_init()
    initCard()
    initPlayer()


    time1 = time.time()
    ####################################### START READY ##############################################
    write1([P,R,E,S,S],5)
    write2([T,O,SP,S,T,A,R,T],5)
    ready_state=False
    ser_input()
    time.sleep(2)
    LED.screen = [[0 for x in range(32)] for x in range(16)]
    write1([SP,SP,A,L,L],5)
    write2([SP,R,E,A,D,Y,ex],5)
    time.sleep(2)

    ####################################### END READY ##############################################
    LED.screen = [[0 for x in range(32)] for x in range(16)] # 게임 시작 전 LED CLEAR!
    who = 0                             # who: 누구차례인지 나타내는 변수, player_list의 index를 나타냄, 처음엔 index 0부터 시작
    while True: # 게임 while문
        if(len(player_list) == 1):  # 게임 종료 조건: 플레이어가 한명 남을 경우 
            react()
            sys.exit()
        if(who != -1): i = who 
        player_list[i].output() 
        check_cards()                   # 5개짜리 있다면, TAKE =1 갱신
        # if(특정키 입력):
        update_label_remaining()  # 특정키 입력시 남은 카드 수 LED 출력 
        keyboard_input()          # 종친 플레이어의 index 반환
        
        if(who == -1):                  # 아무도 종을 안친 경우
            if(len(player_list) < 4):        
                #if(i+1>=len(player_list)):     # 플레이어 한명이 게임에서 진경우 player_list의 길이가 작아짐 그 경우 고려함f
                #    i = i-1
                i = (i+1)%len(player_list)  # 다음 사람~
            else: 
                i = (i+1)%len(player_list)  # 다음 사람~
        else:
            i = who                     # 누가 종친경우 그 사람의 index를 i로! 
            

if __name__ == '__main__':
    main()
