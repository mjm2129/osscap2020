#import LED_display as LED
import threading
import time
import numpy as np
import random
import pygame, pygcurse
from pygame.locals import *
import copy
import os
import sys

iScreen = [[0 for x in range(32)] for x in range(16)]

win = pygcurse.PygcurseWindow(32,16, fullscreen=False)

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
    global p1,p2,p3,p4,present_total_card
    print("p1:",len(p1.hand_cards))
    print("p2:",len(p2.hand_cards))
    print("p3:",len(p3.hand_cards))
    print("p4:",len(p4.hand_cards))
    # print(len(present_total_card))

def lose():
    global p1,p2,p3,p4
    if len(p1.hand_cards) == 0:
        print("p1 lose")
        sys.exit()
    if len(p2.hand_cards) == 0:
        print("p2 lose")
        sys.exit()
    if len(p3.hand_cards) == 0:
        print("p3 lose")
        sys.exit()
    if len(p4.hand_cards) == 0:
        print("p4 lose")
        sys.exit()

def consoleMatrix(screen):
    for i in screen:
        print(i)


def pygcurseMatrix(screen):
    for i in range(16):
        for j in range(32):
            if screen[i][j] == 1:
                win.putchar('@', j, i, 'blue')
            elif screen[i][j] == 2:
                win.putchar('@', j, i, 'green')
            elif screen[i][j] == 3:
                win.putchar('@', j, i, 'yellow')
            elif screen[i][j] == 4:
                win.putchar('@', j, i, 'red')    
            #default color = 'white', 'yellow' ,'fuchsia' ,'red', 'silver', 'gray', 'olive', 'purple', 'maroon', 'aqua', 'lime', 'teal', 'green', 'blue', 'navy', 'black'
    win.update()

def main():
    global card1, card2, card3, card4
    global present_surface_card, present_sum, present_total_card
    global TAKE
    initCard()
    initPlayer()
    os.system('clear' if os.name == 'posix' else 'clear')

    while True:
        oScreen = copy.deepcopy(iScreen)
        win.fill('@', fgcolor='black', bgcolor='black')

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
        #Player1###################################################################
        if len(p1.hand_cards) == 0:  
            lose()                  
        else:
            if card1 is not None:
                present_surface_card[0] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - card1.count
        card1 = p1.hand_cards.pop()
        present_surface_card[0] = [card1]
        present_total_card = present_total_card+[card1]
        for i in range(4):
            present_sum[i] = present_sum[i] + card1.count
            # print("card1's count",card1.count)
        for i in range(8):
                for j in range(16):
                    oScreen[i][j]=card1.coord[i][j]
        pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        time.sleep(0.1) # 입력 받기
        #Player2###################################################################
        if len(p2.hand_cards) == 0: 
            lose()                  
        else:
            if card2 is not None:
                present_surface_card[0] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - card2.count
        card2 = p2.hand_cards.pop()
        present_surface_card[0] = [card2]
        present_total_card = present_total_card+[card2]
        for i in range(4):
            present_sum[i] = present_sum[i] + card2.count
            # print("card2's count",card2.count)
        for i in range(8):
                for j in range(16):
                    oScreen[i][j+16]=card2.coord[i][j]
        # consoleMatrix(oScreen)
        pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        time.sleep(0.1)
        #Player3###################################################################
        if len(p3.hand_cards) == 0:  
            lose()                  
        else:
            if card3 is not None:
                present_surface_card[0] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - card3.count
        card3 = p3.hand_cards.pop()
        present_surface_card[0] = [card3]
        present_total_card = present_total_card+[card3]
        for i in range(4):
            present_sum[i] = present_sum[i] + card3.count
        for i in range(8):
                for j in range(16):
                    oScreen[i+8][j]=card3.coord[i][j]
        # consoleMatrix(oScreen)
        pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        time.sleep(0.1)
        #Player4###################################################################
        if len(p4.hand_cards) == 0:   
            lose()                  
        else:
            if card4 is not None:
                present_surface_card[0] = []
                for i in range(4):
                    present_sum[i] = present_sum[i] - card4.count
        card4 = p4.hand_cards.pop()
        present_surface_card[0] = [card4]
        present_total_card = present_total_card+[card4]
        for i in range(4):
            present_sum[i] = present_sum[i] + card4.count
        for i in range(8):
                for j in range(16):
                    oScreen[i+8][j+16]=card4.coord[i][j]
        # consoleMatrix(oScreen)
        pygcurseMatrix(oScreen)
        check_cards()
        update_label_remaining()
        time.sleep(0.1)

        os.system('clear' if os.name =='posix' else 'clear')

if __name__ == '__main__':
    main()