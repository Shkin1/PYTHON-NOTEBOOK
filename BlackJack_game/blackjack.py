# BLACK JACK - CASINO
'''
游戏玩法: 该游戏由 2 到 6 个人玩，使用除大小王之外的 52 张牌，
游戏者的目标是使手中的牌的点数之和不超过 21 点且尽量大。
有着悠久的历史。黑杰克简称为21点，1700年左右法国赌场就有这种21点的纸牌游戏。
1931年，当美国内华达州宣布赌博为合法活动时，21点游戏第一次公开出现在内华达州的赌场俱乐部，
15年内，它取代掷骰子游戏，而一举成为非常流行的赌场庄家参与的赌博游戏。

'''

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(deck)

print(
    "                       **********************************************************                                    ")
print(
    "                                   Welcome to the game Casino - BLACK JACK (21点)!                                         ")
print(
    "                       **********************************************************                                    ")

d_cards = []  # Initialising dealer's cards
p_cards = []  # Initialising player's cards

while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print('荷官有 X ', d_cards[1])

# Displaying the Player's cards
while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print("你一共 ", str(sum(p_cards)) + "点 :",p_cards)


if sum(p_cards) > 21:
    print("你的点数:",p_cards)
    print("你输了 !\n  **************荷官 Wins !!******************\n")
    exit()

if sum(d_cards) > 21:
    print("荷官的点数:", d_cards)
    print("荷官输了 !\n   ************** You are the Winner !!******************\n")
    exit()

if sum(d_cards) == 21:
    print("荷官的点数:", d_cards)
    print("***********************荷官 is the Winner !!******************")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print("*****************The match is tie 平手!!*************************")
    exit()


def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print("你一共 " + str(sum(p_cards)) + "点 :", p_cards)
    print("荷官一共 " + str(sum(d_cards)) + "点 :", d_cards)

    if sum(p_cards) == sum(d_cards):
        print("***************The match is tie 平手!!****************")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print("***********************Dealer is the Winner !!******************")
        elif sum(p_cards) == 21:
            print("********************There is tie !!**************************")
        else:
            print("***********************Dealer is the Winner !!******************")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print("***********************Dealer is the Winner !!******************")
        if sum(p_cards) == 21:
            print("**********************Player is winner !!**********************")
        if sum(p_cards) < 21 and sum(p_cards) > sum(d_cards):
            print("**********************Player is winner !!**********************")

    else:
        if sum(p_cards) < 21:
            print("**********************Player is winner !!**********************")
        elif sum(p_cards) == 21:
            print("**********************Player is winner !!**********************")
        else:
            print("***********************Dealer is the Winner !!******************")


while sum(p_cards) < 21:

    k = input('Want to hit or stay?\n Press 1 for hit and 0 for stay ')
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print('你的点数:' + str(sum(p_cards)), p_cards)
        if sum(p_cards) > 21:
            print('*************你输了 !*************\n Dealer Wins !!')
        if sum(p_cards) == 21:
            print('*******************你赢了 !!*****************************')


    else:
        dealer_choice()
        break