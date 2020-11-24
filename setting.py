import LED_display as LED
import threading
import keyboard
import time
import numpy as np
import random
import copy
import os


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

    def __init__ (self, player_id = "", time = 0, hand_cards = [], order=0):
        self.player_id = player_id
        self.time = time
        self.hand_cards = hand_cards
        self.order = order

    def output(self):
        global present_surface_card, present_sum,present_total_card, card
        if len(p1.hand_cards) == 0:  
            lose()                  
        else:
            if card is not None:
                present_surface_card[0] = []
                present_sum[card.color-1] = present_sum[card.color-1] - card.count
            card = self.hand_cards.pop()
            present_surface_card[0] = [card1]
            present_total_card = present_total_card+[card]
            present_sum[card.color-1] = present_sum[card.color-1] + card.count
            print("[R G Y B]")
            print(present_sum)
            if(self.order == 1):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i][j]=card.coord[i][j]
            elif(self.order == 2):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i][j+16]=card.coord[i][j]
            elif(self.order == 3):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j]=card.coord[i][j]
            elif(self.order == 4):
                for i in range(8):
                    for j in range(16):
                        LED.screen[i+8][j+16]=card.coord[i][j]
        
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
card = None
p1 = []
p2 = []
p3 = []
p4 = []
player_list=[]

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


def update_label_remaining():
    global p1,p2,p3,p4,present_total_card,present_sum
    print("p1:",len(p1.hand_cards))
    print("p2:",len(p2.hand_cards))
    print("p3:",len(p3.hand_cards))
    print("p4:",len(p4.hand_cards))
    # print(len(present_total_card))
    # print("[R G B Y]")
    # print(present_sum)

def lose():
    global p1,p2,p3,p4, player_list
    if len(p1.hand_cards) == 0:
        print("p1 lose")
        player_list.remove(p1)
    if len(p2.hand_cards) == 0:
        print("p2 lose")
        player_list.remove(p2)
    if len(p3.hand_cards) == 0:
        print("p3 lose")
        player_list.remove(p3)
    if len(p4.hand_cards) == 0:
        print("p4 lose")
        player_list.remove(p4)
    if len(p1.hand_cards)== 56 or len(p2.hand_cards)== 56 or len(p3.hand_cards)== 56 or len(p4.hand_cards)== 56:
        print("all player lose")
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

def keyboard_input():
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
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            # clean_cards()
        elif TAKE == 0:
            if len(p1.hand_cards) > 3:
                p2.hand_cards.insert(0, p1.hand_cards.pop())
                p3.hand_cards.insert(0, p1.hand_cards.pop())
                p4.hand_cards.insert(0, p1.hand_cards.pop())
            else:
                p1.hand_cards = []
                lose()
        '''card1 = p1.hand_cards.pop()
        present_surface_card[0] = [card1]
        present_total_card = present_total_card+[card1]
        present_sum[card1.color-1] = present_sum[card1.color-1] + card1.count
        print("[R G Y B]")
        print(present_sum)
        # print("card1's count",card1.count)
        
        for i in range(8):
            for j in range(16):
                LED.screen[i][j]=card1.coord[i][j]'''
        check_cards()
        update_label_remaining()
    elif event == '2':
        if (TAKE == 1 and RING == 0):
            p2.hand_cards = present_total_card + p2.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            # clean_cards()
        elif TAKE == 0:
            if len(p2.hand_cards) > 3:
                p1.hand_cards.insert(0, p2.hand_cards.pop())
                p3.hand_cards.insert(0, p2.hand_cards.pop())
                p4.hand_cards.insert(0, p2.hand_cards.pop())
            else:
                p2.hand_cards = []
                lose()
        '''card2 = p2.hand_cards.pop()
        present_surface_card[1] = [card2]
        present_total_card = present_total_card+[card2]
        present_sum[card2.color-1] = present_sum[card2.color-1] + card2.count
        print("[R G Y B]")
        print(present_sum)
        # print("card2's count",card2.count)
        for i in range(8):
            for j in range(16):
                LED.screen[i][j+16]=card2.coord[i][j]'''
        check_cards()
        update_label_remaining()
    elif event == '3':
        if (TAKE == 1 and RING == 0):
            p3.hand_cards = present_total_card + p3.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            # clean_cards()
        elif TAKE == 0:
            if len(p3.hand_cards) > 3:
                p1.hand_cards.insert(0, p3.hand_cards.pop())
                p2.hand_cards.insert(0, p3.hand_cards.pop())
                p4.hand_cards.insert(0, p3.hand_cards.pop())
            else:
                p3.hand_cards = []
                lose()
        '''card3 = p3.hand_cards.pop()
        present_surface_card[2] = [card3]
        present_total_card = present_total_card+[card3]
        present_sum[card3.color-1] = present_sum[card3.color-1] + card3.count
        print("[R G Y B]")
        print(present_sum)    
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j]=card3.coord[i][j]'''
        check_cards()
        update_label_remaining()
    elif event == '4':
        if (TAKE == 1 and RING == 0):
            p4.hand_cards = present_total_card + p4.hand_cards
            present_total_card = []
            present_surface_card = [[], [], [], []]
            present_sum = np.asarray([0, 0, 0, 0])
            card1, card2, card3, card4, RING, TAKE = None, None, None, None, 0, 0
            for i in range(16):
                for j in range(32):
                    LED.screen[i][j]=0
            # clean_cards()
        elif TAKE == 0:
            if len(p4.hand_cards) > 3:
                p1.hand_cards.insert(0, p4.hand_cards.pop())
                p2.hand_cards.insert(0, p4.hand_cards.pop())
                p3.hand_cards.insert(0, p4.hand_cards.pop())
            else:
                p4.hand_cards = []
                lose()
        '''card4 = p4.hand_cards.pop()
        present_surface_card[3] = [card4]
        present_total_card = present_total_card+[card4]
        present_sum[card4.color-1] = present_sum[card4.color-1] + card4.count
        print("[R G Y B]")
        print(present_sum)
        for i in range(8):
            for j in range(16):
                LED.screen[i+8][j+16]=card4.coord[i][j]'''
        check_cards()
        update_label_remaining()
    
p1_ready=0
p2_ready=0
p3_ready=0
p4_ready=0
a=0
b=0
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

    #    for event in pygame.event.get():
    #        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
    #                pygame.quit()
    #                sys.exit()
        #Player1###################################################################

    global a
    global p1_ready
    global p2_ready
    global p3_ready
    global p4_ready
    global b

    while True:
        if keyboard.is_pressed('s'):
            print("ready_room")
            b+=1
            break
            
    while b!=0:
        
        if keyboard.is_pressed('1'):
            p1_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i][j]=1
        if keyboard.is_pressed('2'):
            p2_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i][j+8]=2

        if keyboard.is_pressed('3'):
            p3_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i][j+16]=3
            
        if keyboard.is_pressed('4'):
            p4_ready+=1
            for i in range(4):
                for j in range(8):
                    LED.screen[i][j+24]=4
            
            
        if (p1_ready!=0 and p2_ready!=0) and (p3_ready!= 0 and p4_ready!= 0):
            print("all player get ready")
            time.sleep(3)
            a=1
            break

    LED.screen = [[0 for x in range(32)] for x in range(16)]
    while a!=0:
        for a in player_list:
            a.output()
            check_cards()
            update_label_remaining()
            keyboard_input()

'''     p1.output()
        check_cards()
        update_label_remaining()
        # time.sleep(2) # 입력 받기
        keyboard_input()
        #Player2###################################################################
        p2.output()
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard_input()
        #Player3###################################################################
        p3.output()
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard_input()
        #Player4###################################################################
        p4.output()
        check_cards()
        update_label_remaining()
        # time.sleep(2)
        keyboard_input()
        # os.system('clear' if os.name =='posix' else 'clear')'''

if __name__ == '__main__':
    main()
