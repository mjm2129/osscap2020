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
mode = 0
level = 0
HARD = 0.5
NORMAL = 0.65
EASY = 0.75

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

def writecal1(a,b,c,d):
    q=0
    for letter in a:
        for i in range(5):
            for j in range(4):
                if letter[i][j]!=0:
                     LED.screen[i+c][j+d+q]=letter[i][j]+b-1
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

    def __init__ (self, player_id = "", time = 0, hand_cards = [], order=0, card = None, live = True):
        self.player_id = player_id
        self.time = time
        self.hand_cards = hand_cards
        self.order = order
        self.card = card
        self.live = live

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
    global total_card, p1,p2,p3,p4,player_list,mode
    
    empty = []
    # getPlayerName() -> p1.name, p2.name, p3.name, p4.name 
    if(mode == 4):
        p1 = Player("P1", 1.00,total_card[0:14], 1, None, True)
        p2 = Player("P2", 1.00,total_card[14:28], 2, None, True)
        p3 = Player("P3", 1.00,total_card[28:42], 3, None, True)
        p4 = Player("P4", 1.00,total_card[42:], 4, None, True)
        player_list = [p1,p2,p3,p4]
    elif(mode == 1):
        p1 = Player("P1", 1.00,total_card[0:28], 1, None, True)
        p2 = Player("P2", 1.00, empty, 2, None, False)
        p3 = Player("P3", 1.00, empty, 3, None, False)
        p4 = Player("P4", 1.00,total_card[28:], 4, None, True)
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
    global p1,p2,p3,p4, player_list, mode
    if len(p1.hand_cards) == 0 and p1.live == True:
        #print("p1 lose")
        #player_list.remove(p1)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j] = 0
        time.sleep(1)
        p1.live = False           
        p1.card = None     
 
    if len(p2.hand_cards) == 0 and p2.live == True:
        #print("p2 lose")
        #player_list.remove(p2)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j+16] = 0 
        time.sleep(1)
        p2.live = False       
        p2.card = None         

    if len(p3.hand_cards) == 0 and p3.live == True:
        #print("p3 lose")
        #player_list.remove(p3)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j] = 0 
        time.sleep(1)
        p3.live = False            
        p3.card = None    
 

    if len(p4.hand_cards) == 0 and p4.live == True:
        #print("p4 lose")
        #player_list.remove(p4)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16] = 0 
        time.sleep(1)
        p4.live = False    
        p4.card = None                
    print(p1.live, p2.live, p3.live, p4.live)
    cnt=0
    for i in range(len(player_list)):
        if player_list[i].live==True:
            cnt=cnt+1
    if cnt==1:
        if(mode == 4):
            react()
        elif(mode == 1):
            win_p1()
        sys.exit()
##################################################################



def lose():
    global p1,p2,p3,p4, player_list, mode
    if len(p1.hand_cards) == 0 and p1.live == True:
        #print("p1 lose")
        #player_list.remove(p1) 
        for i in range(8):
            for j in range(16):
                LED.screen[i][j] = 0
        time.sleep(1)
        p1.live = False
        
        cnt=0
        for i in range(len(player_list)):
            if player_list[i].live==True:
                cnt=cnt+1
        if cnt==1:
            if(mode == 4):
                react()
            elif(mode == 1):
                win_p1()
            sys.exit()
        
        if(p1.card != None):
            present_sum[p1.card.color-1] = present_sum[p1.card.color-1] - p1.card.count
        p1.card = None     
 
    if len(p2.hand_cards) == 0 and p2.live == True:
        #print("p2 lose")
        #player_list.remove(p2)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j+16] = 0 
        time.sleep(1)
        p2.live = False
        cnt=0
        for i in range(len(player_list)):
            if player_list[i].live==True:
                cnt=cnt+1
        if cnt==1:
            if(mode == 4):
                react()
            elif(mode == 1):
                win_p1()
            sys.exit()  
        if (p2.card != None):     
            present_sum[p2.card.color-1] = present_sum[p2.card.color-1] - p2.card.count
        p2.card = None         

    if len(p3.hand_cards) == 0 and p3.live == True:
        #print("p3 lose")
        #player_list.remove(p3)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j] = 0 
        time.sleep(1)
        p3.live = False     
        cnt=0
        for i in range(len(player_list)):
            if player_list[i].live==True:
                cnt=cnt+1
        if cnt==1:
            if(mode == 4):
                react()
            elif(mode == 1):
                win_p1()
            sys.exit()       
        if(p3.card != None):
            present_sum[p3.card.color-1] = present_sum[p3.card.color-1] - p3.card.count
        p3.card = None    
 

    if len(p4.hand_cards) == 0 and p4.live == True:
        #print("p4 lose")
        #player_list.remove(p4)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16] = 0 
        time.sleep(1)
        p4.live = False  
        cnt=0
        for i in range(len(player_list)):
            if player_list[i].live==True:
                cnt=cnt+1
        if cnt==1:
            if(mode == 4):
                react()
            elif(mode == 1):
                win_p1()
            sys.exit()  
        if(p4.card != None):
            present_sum[p4.card.color-1] = present_sum[p4.card.color-1] - p4.card.count
        p4.card = None                
    print(p1.live, p2.live, p3.live, p4.live)
    cnt=0
    for i in range(len(player_list)):
        if player_list[i].live==True:
            cnt=cnt+1
    if cnt==1:
        if(mode == 4):
            react()
        elif(mode == 1):
            win_p1()
        sys.exit()

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

def sensor_input():
    while True:
        #print("while")
        if ser.readable():
            ser.flushInput()
            read = ser.readline()
            read2 = read.decode('utf8', 'ignore')[:len(read)-1].split()

            if(len(read2) < 4):
                continue
            
            if int(read2[0])+int(read2[1])+int(read2[2])+int(read2[3])<30:
                flag=0
            if int(read2[0])> 150 :
                print(read2[0])
                what = 1
                return what
            if int(read2[1])> 150 :
                print(read2[1])
                what = 2
                return what
            if int(read2[2])> 150 :
                print(read2[2])
                what = 3
                return what
            if int(read2[3])> 150 :
                print(read2[3])
                what = 4
                return what

def ser_input():
    global ser_who, time1, t1, t2, t3, t4, check, ready_state, p1_ready, p2_ready, p3_ready, p4_ready
    ser_who = -1
    global flag, flag1, flag2, flag3, flag4, calm, level
    if ready_state == False:
        t=9999
    else:
        t=1
    while time.time() - time1 < t :
        #print("while")
        if ser.readable():
            ser.flushInput()
            read = ser.readline()
            read2 = read.decode('utf8', 'ignore')[:len(read)-1].split()

            if(len(read2) < 4):
                continue
            if ready_state == False:
                write1([P,R,E,S,S],5)
                write2([T,O,SP,S,T,A,R,T],5)
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
                if (mode == 1):
                    if(time.time() - time1 >= level):
                        print(time.time() - time1)
                        read2[3] = 200 #computer always push button
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
    global TAKE, who, ser_who, time1, t1, t2, t3, t4, mode
    
    #time1 = time.time()
    ser_input()
    if(mode == 4):
        if (ser_who == 1 and p1.live==True):
            if (TAKE == 1):
                p1.time = float(format(min(t1, p1.time),".3f"))
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
                t1 = float(format(t1,".3f"))
                printgoodgameset(num_1,t1 , len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
            elif TAKE == 0:
                if len(p1.hand_cards) > len(player_list)-1:
                    for i in range(len(player_list)):
                        if i == player_list.index(p1):
                            continue
                        if player_list[i].live == False:
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
                p2.time = float(format(min(t2, p2.time),".3f"))
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
                t2 = float(format(t2,".3f"))
                printgoodgameset(num_2, t2, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
            elif TAKE == 0:
                if len(p2.hand_cards) > len(player_list)-1:
                    for i in range(len(player_list)):
                        if i == player_list.index(p2):
                            continue
                        if player_list[i].live == False:
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
                p3.time = float(format(min(t3, p3.time),".3f"))
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
                t3 = float(format(t3,".3f"))
                printgoodgameset(num_3, t3, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
                # clean_cards()
            elif TAKE == 0:
                if len(p3.hand_cards) > len(player_list)-1:
                    for i in range(len(player_list)):
                        if i == player_list.index(p3):
                            continue
                        if player_list[i].live == False:
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
                p4.time = float(format(min(t4, p4.time),".3f"))
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
                t4 = float(format(t4,".3f"))
                printgoodgameset(num_4, t4, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
            elif TAKE == 0:
                if len(p4.hand_cards) > len(player_list)-1:
                    for i in range(len(player_list)):
                        if i == player_list.index(p4):
                            continue
                        if player_list[i].live == False:
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

    elif(mode == 1):
        if (ser_who == 1 and p1.live==True):
            if (TAKE == 1):
                p1.time = float(format(min(t1, p1.time),".3f"))
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
                t1 = float(format(t1,".3f"))
                printgoodgameset(num_1,t1 , len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
            elif TAKE == 0:
                if len(p1.hand_cards) > len(player_list)-1:
                    for i in range(len(player_list)):
                        if i == player_list.index(p1):
                            continue
                        if player_list[i].live == False:
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

        elif (ser_who == 4 and p4.live==True):
            if (TAKE == 1):
                p4.time = float(format(min(t4, p4.time),".3f"))
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
                t4 = float(format(t4,".3f"))
                printgoodgameset(num_4, t4, len(p1.hand_cards), len(p2.hand_cards), len(p3.hand_cards), len(p4.hand_cards))
                gamesetlose()
            elif TAKE == 0:
                time.sleep(1-level)
                who = -1
                return

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
                for spzks in letter:
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
            time.sleep(0.15)
            for a in range(15):
                for b in range(32):
                    LED.screen[a][b]=LED.screen[a+1][b]
                    LED.screen[a+1][b]=0

def react():
    global p1,p2,p3,p4, player_list
    global React, file_line
    text_file = open("test.txt", "r")
    file_line=text_file.readlines()
    React.append(format(p1.time,".3f"))
    React.append(format(p2.time,".3f"))
    React.append(format(p3.time,".3f"))
    React.append(format(p4.time,".3f"))
    txt_line=file_line
    for i in range(4):
        for j in range(10):
            if file_line[j][0]!='P':
                continue
            elif float(React[i])<float(file_line[j][3:8]):
                txt_line.insert(j,'P'+str(i+1)+' '+str(React[i])+'\n')
                del file_line[10]
                break
    '''
    player = None
    for player in player_list:
        if( player.live == True):
            break
    '''

    for i in range(16):
        for j in range(32):
            LED.screen[i][j] = 0 
    for i in range(len(player_list)):
        if(player_list[i].live == True):
            char = player_list[i].player_id[1]
            print(char,"win")
            break

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
    print(txt_line)
    timemoveprint(txt_line)

def win_p1():
    global player_list
    for i in range(16):
        for j in range(32):
            LED.screen[i][j] = 0 
    for i in range(len(player_list)):
        if(player_list[i].live == True):
            char = player_list[i].player_id[1]
            print(char,"win")
            break

    if(char == '1') : write1([P,num_1,SP,W,I,N,ex],7)
    if(char == '2') : write1([P,num_2,SP,W,I,N,ex],7)
    if(char == '3') : write1([P,num_3,SP,W,I,N,ex],7)
    if(char == '4') : write1([P,num_4,SP,W,I,N,ex],7)
    time.sleep(2)

    
def main():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE, who, ser_who, ready_state, time1, mode, level
    LED_init()
    initCard()
    # print("select 4P or 1P:")
    # ans = input()
    # if(ans == "1P"):
    #     mode = 1
    # elif(ans == "4P"):
    #     mode = 4
    write1([SP,M,O,D,E],6)
    write2([num_1,P,SP,O,R,SP,num_4,P],6)
    ready_state = True
    while True:
        mode = sensor_input()
        if(mode == 1 or mode == 4):
            break
    print("mode",mode)
    initPlayer()
    LED.screen = [[0 for x in range(32)] for x in range(16)]
    time.sleep(1)
    ####################################### START READY ##############################################
    if( mode == 4):
        ready_state=False
        time1 = time.time()
        ser_input()
        time.sleep(2)
        LED.screen = [[0 for x in range(32)] for x in range(16)]
        write1([SP,SP,A,L,L],5)
        write2([SP,R,E,A,D,Y,ex],5)
        time.sleep(2)
    elif(mode == 1):
        # LED.screen = [[0 for x in range(32)] for x in range(16)]
        write1([S,I,N,G,L,E], 6)
        write2([SP,M,O,D,E,ex],6)
        time.sleep(2)
        LED.screen = [[0 for x in range(32)] for x in range(16)]
        writecal1([num_1,dot,H,A,R,D],1,0,0)
        writecal1([num_2,dot,N,O,R,M,A,L],2,5,0)
        writecal1([num_3,dot,E,A,S,Y],3,10,0)
        while True:
            abc = sensor_input()
            if(abc == 1 or abc == 2 or abc ==3):
                break

        if(abc == 1):
            level = HARD
        if(abc == 2):
            level = NORMAL
        if(abc == 3):
            level = EASY
        time.sleep(1)
        ready_state = True
    
    ####################################### END READY ##############################################
    LED.screen = [[0 for x in range(32)] for x in range(16)] # 게임 시작 전 LED CLEAR!
    who = 0                             # who: 누구차례인지 나타내는 변수, player_list의 index를 나타냄, 처음엔 index 0부터 시작
    i = 0
    while True: # 게임 while문
        #if(who != -1): i = who 
        
        if player_list[i].live==False:
            i = (i+1) % len(player_list)
            continue
        player_list[i].output() 
        
        check_cards()                   # 5개짜리 있다면, TAKE =1 갱신
        update_label_remaining()  # 특정키 입력시 남은 카드 수 LED 출력 
        keyboard_input()          # 종친 플레이어의 index 반환
        
        if(who == -1):
            i = (i+1) % len(player_list)
        else:
            i = who                     # 누가 종친경우 그 사람의 index를 i로! 
            

if __name__ == '__main__':
    main()
