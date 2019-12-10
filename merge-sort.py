#!/usr/bin/env python3

import random
import time

def merge_sort(l):
    if len(l) == 1:
        return l

    middle = len(l) // 2

    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1

    return l

for n in range(10):
    random.seed(time.time())
    input = [random.randrange(0, 99) for _ in range(random.randrange(1, 30))]
    assert(merge_sort(input) == merge_sort(input))
