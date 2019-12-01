#!/usr/bin/env python3
#
# Challenge: RoboScript #2 - Implement the RS1 Specification
# Url: https://www.codewars.com/kata/5870fa11aa0428da750000da

def render_grid(grid):
    x_max = max(grid.keys())
    x_min = min(grid.keys())
    y_max = max(max(s) for s in grid.values())
    y_min = min(min(s) for s in grid.values())

    lines = []

    for y in range(y_max, y_min - 1, -1):
        line = ""
        for x in range(x_min, x_max + 1):
            if x in grid and y in grid[x]:
                line += "*"
            else:
                line += " "

        lines.append(line)

    return "\r\n".join(lines)


def execute(code):
    commands = ""
    command = ""
    multiplier = ""

    for s in code:
        if s.isnumeric():
            multiplier += s

        elif command:
            if multiplier:
                commands += command * int(multiplier)
                multiplier = ""
            else:
                commands += command

            command = s

        else:
            command = s

    if multiplier:
        commands += command * int(multiplier)
        multiplier = ""
    else:
        commands += command

    x = 0
    y = 0

    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    grid = {0: set([0])}

    for c in commands:
        if c == "F":
            x += direction[0][0]
            y += direction[0][1]

            grid.setdefault(x, set()).add(y)

        if c == "R":
            direction = direction[1:] + [direction[0]]

        if c == "L":
            direction = [direction[-1]] + direction[0:-1]


    return render_grid(grid)


execute("F4RF4LF4LF3L10")

# From Blind4Basics, aenik97
#
# from collections import deque
# import re
#
# TOKENIZER = re.compile(r'(R+|F+|L+)(\d*)')
#
# def execute(code):
#
#     pos, dirs = (0,0), deque([(0,1), (1,0), (0,-1), (-1,0)])
#     seens = {pos}
#
#     for act,n in TOKENIZER.findall(code):
#         s,r = act[0], int(n or '1') + len(act)-1
#
#         if s == 'F':
#             for _ in range(r):
#                 pos = tuple( z+dz for z,dz in zip(pos, dirs[0]) )
#                 seens.add(pos)
#         else:
#             dirs.rotate( (r%4) * (-1)**(s == 'R') )
#
#     miX, maX = min(x for x,y in seens), max(x for x,y in seens)
#     miY, maY = min(y for x,y in seens), max(y for x,y in seens)
#
#     return '\r\n'.join( ''.join('*' if (x,y) in seens else ' ' for y in range(miY, maY+1))
#                         for x in range(miX, maX+1) )
