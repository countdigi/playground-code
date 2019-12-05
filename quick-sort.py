#!/usr/bin/env python3

import unittest

class Test(unittest.TestCase):
    def test_partition(self):
        a = [3, 2, 1, 7, 6, 4, 5]

        pivot_index = partition(a, 0, len(a) - 1)

        self.assertEqual(a, [3, 2, 1, 4, 5, 7, 6])
        self.assertEqual(pivot_index, 4)

    def test_quicksort(self):
        a = [3, 2, 1, 7, 6, 4, 5]
        quicksort(a, 0, len(a) - 1)

        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])


def quicksort(a, start, end):
    if start < end:
        pivot_index = partition(a, start, end)
        quicksort(a, start, pivot_index - 1)
        quicksort(a, pivot_index + 1, end)


def partition(a, start, end):
    pivot_index = end
    i = start - 1

    for j in range(start, end):
        if a[j] < a[pivot_index]:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[pivot_index] = a[pivot_index], a[i+1]

    return i + 1


if __name__ == "__main__":
    unittest.main()
