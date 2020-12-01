import threading
import time
import numpy as np
import random

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
    def __init__ (self, player_id = "", time = 0, hand_cards = []):
        self.player_id = player_id
        self.time = time
        self.hand_cards = hand_cards


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


total_card = [] #리스트형의 전체 카드
present_sum = np.asarray([0,0,0,0]) # 각 카드에 대한 그림 개수 저장
present_surface_card = [[],[],[],[]]
present_total_card = [] # 필드에 있는 사용자들의 모든 카드
p1=[]
p2=[]
p3=[]
p4=[]

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
    global total_card, p1,p2,p3,p4
    # getPlayerName() -> p1.name, p2.name, p3.name, p4.name 
    p1 = Player("P1", 0,total_card[0:14])
    p2 = Player("P2", 0,total_card[14:28])
    p3 = Player("P3", 0,total_card[28:42])
    p4 = Player("P4", 0,total_card[42:])



def check_cards():
    global present_sum, TAKE
    # 检查在场牌数
    if 5 in present_sum:
        TAKE = 1  # 可拍铃
    else:
        TAKE = 0
    print(present_sum,present_surface_card,RING,TAKE)


def update_label_remaining():
    global p1,p2,p3,p4
    print("p1:",len(p1.hand_cards))
    print("p2:",len(p2.hand_cards))
    print("p3:",len(p3.hand_cards))
    print("p4:",len(p4.hand_cards))

def lose():
    global p1,p2,p3,p4
    if not p1.hand_cards:
        print("p1 lose")
    if not p2.hand_cards:
        print("p2 lose")
    if not p3.hand_cards:
        print("p3 lose")
    if not p4.hand_cards:
        print("p4 lose")

React=[]
F=[]

def react():
    global p1,p2,p3,p4
    p1.time=0.12
    p2.time=2.268
    p3.time=0.03
    p4.time=1.32
    global React, F
    text_file = open("test.txt", "r")
    F=text_file.readlines()
    React.append(format(p1.time,".3f"))
    React.append(format(p2.time,".3f"))
    React.append(format(p3.time,".3f"))
    React.append(format(p4.time,".3f"))
    T=F
    for i in range(4):
        for j in range(10):
            if F[j][0]!='P':
                continue
            elif float(React[i])<float(F[j][3:8]):
                T.insert(j,'P'+str(i+1)+' '+ React[i] +'\n')
                del F[10]
                break
    print(T)
    text_file = open("test.txt", "w")
    for i in range(10):
        data=T[i]
        text_file.write(data)
    React=[]
        
initCard()
initPlayer()
react()
