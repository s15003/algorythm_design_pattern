#!/usr/bin/python3
LIST_COUNT = 1000
LOOP_COUNT = 1000
MAX_NUM = 1000

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)] 

"""
def selection_sort(data):
    for i in range(len(data) - 1):
        minimum = i
	
        for t in range(i + 1, len(data)):
            if data[minimum] > data[t]:
                minimum = t

        data[i], data[minimum] = data[minimum],  data[i]
"""


"""
def bubble_sort(data):
    for i in range(len(data)):
        for t in range(2, len(data) - i + 1):
            if data[i] < data[t-1]. data[]
"""

"""
def insertion_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        if data[i-1] > tmp:
            j = i
            while j > 0  && data[j-1] > tmp:
                data[j] = data[j-1]
                j -= 1
            data[j] = tmp
"""

"""
def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            tmp = data[i]
            j = i - gap
            while j >= 0 and tmp < data[j]:
                data[]
"""

if __name__ == '__main__':
    import time
    import sys

    start = time.time()
    
    for _ in range(LOOP_COUNT):
        data = data_generate()
        selection_sort(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('平均時間', (end-start))
    print('経過時間', (end-start) / LOOP_COUNT)
