import LED_display as LED
import threading
import time
import numpy as np
import random
#import pygame, pygcurse
#from pygame.locals import *
import copy
import os
import sys

iScreen = [[0 for x in range(32)] for x in range(16)]

#win = pygcurse.PygcurseWindow(32,16, fullscreen=False)

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
    # print(present_sum,present_surface_card,RING,TAKE)


def update_label_remaining():
    global p1,p2,p3,p4,present_total_card,present_sum
    # print("p1:",len(p1.hand_cards))
    # print("p2:",len(p2.hand_cards))
    # print("p3:",len(p3.hand_cards))
    # print("p4:",len(p4.hand_cards))
    # print(len(present_total_card))
    # print("[R G B Y]")
    # print(present_sum)

def lose():
    global p1,p2,p3,p4
    if len(p1.hand_cards) == 0:
        print("p1 lose")
    if len(p2.hand_cards) == 0:
        print("p2 lose")
    if len(p3.hand_cards) == 0:
        print("p3 lose")
    if len(p4.hand_cards) == 0:
        print("p4 lose")
    react()
    sys.exit()

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

React=[]
F=[]

def react():
    global p1,p2,p3,p4
    p1.time=0.123
    p2.time=2.268
    p3.time=0.038
    p4.time=1.322
    global React, F
    text_file = open("test.txt", "r")
    F=text_file.readlines()
    React.append(p1.time)
    React.append(p2.time)
    React.append(p3.time)
    React.append(p4.time)
    T=F
    for i in range(4):
        for j in range(10):
            if F[j][0]!='P':
                continue
            elif React[i]<float(F[j][3:8]):
                T.insert(j,'P'+str(i+1)+' '+str(React[i])+'\n')
                del F[10]
                break
    print(T)
    text_file = open("test.txt", "w")
    for i in range(10):
        data=T[i]
        text_file.write(data)
    React=[]

def keyboard():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE, RING

    event = input()
    if event == '1':
        if (TAKE == 1 and RING == 0):
            p1.hand_cards = present_total_card + p1.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            # clean_cards()
        elif TAKE == 0:
            if len(p1.hand_cards) > 3:
                p2.hand_cards.insert(0, p1.hand_cards.pop())
                p3.hand_cards.insert(0, p1.hand_cards.pop())
                p4.hand_cards.insert(0, p1.hand_cards.pop())
            else:
                p1.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
    elif event == '2':
        if (TAKE == 1 and RING == 0):
            p2.hand_cards = present_total_card + p2.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            # clean_cards()
        elif TAKE == 0:
            if len(p2.hand_cards) > 3:
                p1.hand_cards.insert(0, p2.hand_cards.pop())
                p3.hand_cards.insert(0, p2.hand_cards.pop())
                p4.hand_cards.insert(0, p2.hand_cards.pop())
            else:
                p2.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
    elif event == '3':
        if (TAKE == 1 and RING == 0):
            p3.hand_cards = present_total_card + p3.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            # clean_cards()
        elif TAKE == 0:
            if len(p3.hand_cards) > 3:
                p1.hand_cards.insert(0, p3.hand_cards.pop())
                p2.hand_cards.insert(0, p3.hand_cards.pop())
                p4.hand_cards.insert(0, p3.hand_cards.pop())
            else:
                p3.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
    elif event == '4':
        if (TAKE == 1 and RING == 0):
            p4.hand_cards = present_total_card + p4.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            # clean_cards()
        elif TAKE == 0:
            if len(p4.hand_cards) > 3:
                p1.hand_cards.insert(0, p4.hand_cards.pop())
                p2.hand_cards.insert(0, p4.hand_cards.pop())
                p3.hand_cards.insert(0, p4.hand_cards.pop())
            else:
                p4.hand_cards = []
                lose()
        check_cards()
        update_label_remaining()
    

def main():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE
    LED_init()
    initCard()
    initPlayer()
    #os.system('clear' if os.name == 'posix' else 'clear')
    #oScreen = copy.deepcopy(iScreen)
    #win.fill('@', fgcolor='black', bgcolor='black')
    while True:
    #    for event in pygame.event.get():
    #        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
    #                pygame.quit()
    #                sys.exit()
        #Player1###################################################################
        if len(p1.hand_cards) == 0:  
            lose()                  
        else:
            if card1 is not None:
                present_surface_card[0] = []
                present_sum[card1.color-1] = present_sum[card1.color-1] - card1.count
            # present_sum = np.asarray([0,0,0,0])
            card1 = p1.hand_cards.pop()
            present_surface_card[0] = [card1]
            present_total_card = present_total_card+[card1]
            present_sum[card1.color-1] = present_sum[card1.color-1] + card1.count
            print("[R G Y B]")
            print(present_sum)
            # print("card1's count",card1.count)
            
            for i in range(8):
                    for j in range(16):
                        LED.screen[i][j]=card1.coord[i][j]
            #pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        # time.sleep(2) # 입력 받기
        keyboard()
        #Player2###################################################################
        if len(p2.hand_cards) == 0: 
            lose()                  
        else:
            if card2 is not None:
                present_surface_card[1] = []
                present_sum[card2.color-1] = present_sum[card2.color-1] - card2.count
            card2 = p2.hand_cards.pop()
            present_surface_card[1] = [card2]
            present_total_card = present_total_card+[card2]
            present_sum[card2.color-1] = present_sum[card2.color-1] + card2.count
            print("[R G Y B]")
            print(present_sum)
                # print("card2's count",card2.count)
            for i in range(8):
                    for j in range(16):
                        LED.screen[i][j+16]=card2.coord[i][j]
            # consoleMatrix(oScreen)
            #pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard()
        #Player3###################################################################
        if len(p3.hand_cards) == 0:  
            lose()                  
        else:
            if card3 is not None:
                present_surface_card[0] = []
                present_sum[card3.color-1] = present_sum[card3.color-1] - card3.count
            card3 = p3.hand_cards.pop()
            present_surface_card[2] = [card3]
            present_total_card = present_total_card+[card3]
            present_sum[card3.color-1] = present_sum[card3.color-1] + card3.count
            print("[R G Y B]")
            print(present_sum)
            
            for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j]=card3.coord[i][j]
            # consoleMatrix(oScreen)
#            pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard()
        #Player4###################################################################
        if len(p4.hand_cards) == 0:   
            lose()                  
        else:
            if card4 is not None:
                present_surface_card[0] = []
                present_sum[card4.color-1] = present_sum[card4.color-1] - card4.count
            card4 = p4.hand_cards.pop()
            present_surface_card[3] = [card4]
            present_total_card = present_total_card+[card4]
            present_sum[card4.color-1] = present_sum[card4.color-1] + card4.count
            print("[R G Y B]")
            print(present_sum)
            for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j+16]=card4.coord[i][j]
            # consoleMatrix(oScreen)
            #pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard()
        # os.system('clear' if os.name =='posix' else 'clear')

if __name__ == '__main__':
    main()
