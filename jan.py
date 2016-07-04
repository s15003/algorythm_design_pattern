#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import time
import random



def junken1():
    #じゃんけんの手
    GU = 1
    CHOKI = 2
    PA = 3
    DRAW = 1
    WIN = 2
    LOSE = 3

    #ユーザーが手を選ぶ
    user = random.randint( 1, 3)
    #コンピューターが手を選ぶ
    computer = random.randint( 1, 3)

    #勝敗を判定する
    judge = -1
    if user == GU and computer == GU: judge = DRAW
    elif user == GU and computer == CHOKI: judge = WIN
    elif user == GU and computer == PA: judge = LOSE
    elif user == CHOKI and computer == GU: judge = LOSE
    elif user == CHOKI and computer == CHOKI: judge = DRAW
    elif user == CHOKI and computer == PA: judge = WIN
    elif user == PA and computer == GU: judge = WIN
    elif user == PA and computer == PA: judge = DRAW

def junken2():
    GU = 1
    CHOKI = 2
    PA = 3
    DRAW = 1
    WIN = 2
    LOSE = 3

    user = random.randint( 1, 3)

    computer = random.randint( 1, 3)

    if user == computer: judge = DRAW
    elif ( user == GU and computer == CHOKI) or\
        ( user == CHOKI and computer == PA) or\
        ( user == PA and computer == GU):
        judge = WIN
    else: judge = LOSE

# 結果を表示する

def junken3():
    GU = 1
    CHOKI = 2
    PA = 3
    WIN = 2
    LOSE = 3
# ユーザーが手を選ぶ
    user = random.randint( 1, 3)

# コンピュータが手を選ぶ
    computer = random.randint( 1, 3)

# 勝敗の判定
    judge = ( user - computer + 3) % 3

# 結果を表示する

def junken4():
    GU = 1
    CHOKI = 2
    PA = 3
    DRAW = 1
    WIN = 2
    LOSE = 3
    judge_list = [
        [ DRAW, WIN, LOSE ],
        [ LOSE, DRAW, WIN ],
        [ WIN, LOSE, DRAW ],
        ]
# ユーザーが手を選ぶ
    user = random.randint( 1, 3)
# コンピュータが手を選ぶ
    computer = random.randint( 1, 3)

# 勝敗を判定する
    judge =  judge_list[ user - 1][ computer - 1]

def speed_test(fnc, loop_count, msg):
    print(msg)
    start = time.time()
    for x in range(loop_count):
        fnc()
    end = time.time()
    print('経過時間 : ', end - start)
    print('-------------------------------------')

LOOP_COUNT = 100000

def main():
    speed_test(junken1, LOOP_COUNT, "1個目")
    speed_test(junken2, LOOP_COUNT, "2個目")
    speed_test(junken3, LOOP_COUNT, "3個目")
    speed_test(junken4, LOOP_COUNT, "4個目")

if __name__ == '__main__':
    main()
