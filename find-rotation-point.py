#!/usr/bin/env python3

"""
You are given a list of words that are sorted, however at a certain point in the list
the entries are rotated to the beginning of the list. Find the index point at which
the rotation starts and return 0 if there is no rotation.  E.g.:

    [ 'd', 'e', 'f', 'a', 'b', 'c'] => 3
    [ 'a', 'b', 'c', 'd', 'e', 'f'] => 0

Note the algorithm should perform in O(log n).
"""

import unittest

def find_rotation_point(l):
    start = 0
    end = len(l) - 1

    if end == 0:
        return 0

    while start < end:
        pivot = start + (end - start) // 2

        print(pivot, start, end)

        if l[start] > l[pivot]:
            end = pivot
        else:
            start = pivot

        if start + 1 == end:
            if l[start] > l[end]:
                return end
            else:
                return start


class Test(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(find_rotation_point([ 'd', 'e', 'f', 'a', 'b', 'c']), 3)
        self.assertEqual(find_rotation_point([ 'a']), 0)
        self.assertEqual(find_rotation_point([ 'a', 'b']), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
