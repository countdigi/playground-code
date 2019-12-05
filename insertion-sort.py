#!/usr/bin/env python3

# The general idea is partition the list into a sorted and unsorted size.
# Move up the list taking the current value at the beginning each iteration
# and with a second pointer move down shifting elements up until you find
# the point to put the current value below
#
#

def insertion_sort(a):
    for i in range(1, len(a)):
        current = a[i]

        j = i

        while j > 0 and current < a[j-1]:
           a[j] = a[j - 1]
           j = j - 1

        a[j] = current

    return a


a = [5, 4, 2, 3, 2, 1]

print(insertion_sort(a))


