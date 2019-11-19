#!/usr/bin/env python3
#
# Challenge: RoboScript #2 - Implement the RS1 Specification
# Url: https://www.codewars.com/kata/5870fa11aa0428da750000da

import unittest

#class Test(unittest.TestCase):
#     def test_1(self):
#         q = []
#         self.assertEqual(update_quadrant(q, 1, 1), [[0, 0], [0, 1]])
#
#     def test_2(self):
#         q = []
#         self.assertEqual(update_quadrant(q, 0, 0), [[1]])
#
#     def test_3(self):
#         q = []
#         self.assertEqual(update_quadrant(q, 0, 2), [[0,0,1]])
#
#     def test_4(self):
#         q = []
#         self.assertEqual(update_quadrant(q, 2, 0), [[0], [0], [1]])
#
#     def test_5(self):
#         q = [[0,0],[0,0],[0,1]]
#         self.assertEqual(update_quadrant(q, 1, 2), [[0,0,0], [0,0,1], [0,1,0]])
#
#
#
#    1
#  0 0 1
#  0 0 0

# -2 -1 0 | 0 1 2 3

def render_grid(grid):
    x_max = max(grid.keys())
    x_min = min(grid.keys())
    y_max = max(max(s) for s in grid.values())
    y_min = min(min(s) for s in grid.values())

    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            if x in grid and y in grid[x]:
                print("*", end="")
            else:
                print (" ", end="")

        print("")


def execute(code):
    x = 0
    y = 0

    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    grid = {0: set([0])}

    for c in code:
        if c == "F":
            x += direction[0][0]
            y += direction[0][1]

            grid.setdefault(x, set()).add(y)

        if c == "R":
            direction = direction[1:] + [direction[0]]

        if c == "L":
            direction = [direction[-1]] + direction[0:-1]

    render_grid(grid)

execute("FFFFRFFFFLFFFFLFFFFLFFFFFFFFFFFFFFFF")

#grid = {0: set([0, 1]), 1: set([0, 1, 2])}
#render_grid(grid)



# def update_quadrant(q, x, y):
#     if x + 1 > len(q):
#         for i in range(len(q), x + 1):
#             q.append([])
#
#             for j in range(0, y + 1):
#                 q[i].append(0)
#
#     if y + 1 > len(q[0]):
#         for i in range(0, len(q)):
#             for j in range(len(q[i]), y + 1):
#                  q[i].append(0)
#
#     q[x][y] = 1
#
#     return q
#

# def execute(code):
#     # Quadrants:
#     #
#     # q2|q1
#     # q3|q4
#
#     q1, q2, q3, q4 = [[1]], [[]], [[]], [[]]
#
#     # x, y offsets:
#     #
#     # x=1,y=0  right
#     # x-1,y=0  left
#     # x=0,y=1  up
#     # x=0,y=-1 down
#
#     # if
#     #
#     #         2
#     #  -2 -1  1 2
#     #        -1
#     #        -2
#
#     x_offset = 1
#     y_offset = 0
#
#     output = ""
#
#     x = 0
#     y = 0
#
#     for c in code:
#         if c == "F":
#             x += x_offset
#             y += y_offset
#
#
#         if x >= 0 and y >= 0:  # q1
#             if x < len(q1):
#                 q1[x] = 1
#
#             if y < len(q1[x]):
#                 q1[x][y] = 1
#
#
#         elif y >= 0 and x < 0: # q2
#
#         elif y < 0 and x < 0:  # q3
#
#         elif y < 0 and x >= 0: # q4
#
#
#         output += ("*")
#
#     return output

# if __name__ == "__main__":
#     unittest.main()
#




