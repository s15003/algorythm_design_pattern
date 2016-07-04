#!/usr/bin/python3
# -*- coding: utf-8 -*-


LIST_COUNT = 1000
LOOP_COUNT = 1000
MAX_NUM = 1000

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

def quick_sort(data):
    if len(data) < 1:
        return data

    pivot = data[0]
    left = []
    right = []
    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

if __name__ == '__main__':
    import time
    import sys

    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('平均時間', (end-start))
    print('経過時間', (end-start) / LOOP_COUNT)

def quick_sort2(data):
    if len(data) < 1:
        return data

    pivot = data[0]

    if len(data) > 2:
        pivot = data[0] if data[0] < data[1] else data[1]

    left = []
    right = []
    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort2(left)
    right = quick_sort2(right)

    return left + [pivot] + right

if __name__ == '__main__':
    import time
    import sys

    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort2(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('平均時間', (end-start))
    print('経過時間', (end-start) / LOOP_COUNT)


def quick_sort3(data):
    if len(data) == 0:
        return []

    pivot = data.pop()
    return quick_sort3([x for x in data if x < pivot]) + [pivot] + quick_sort3([x for x in data if x >= pivot])

if __name__ == '__main__':
    import time
    import sys

    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort3(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('平均時間', (end-start))
    print('経過時間', (end-start) / LOOP_COUNT)
