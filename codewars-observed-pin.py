#!/usr/bin/env python3
#
# https://www.codewars.com/kata/the-observed-pin/train/python

import unittest
import itertools

def get_pins(sequence):

    grid = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            [None, '0', None]]

    rows, cols = len(grid), len(grid[0])

    possible = {}

    for x in range(rows):
        for y in range(cols):
            if grid[x][y]:
                possible[grid[x][y]] =  [grid[x][y]] + [grid[a][b] for (a,b) in [(x+1,y), (x, y+1), (x-1, y), (x, y-1)] if a >= 0 and a < rows and b >= 0 and b < cols and grid[a][b]]

    inputs = [possible[s] for s in sequence]

    return [''.join(t) for t in itertools.product(*inputs)]



class Test(unittest.TestCase):

    def test(self):
        expectations = [
                ('8', ['5', '7', '8', '9', '0']),
                ('11', ['11', '22', '44', '12', '21', '14', '41', '24', '42']),
                ('369', ['339','366','399','658','636','258','268','669','668','266','369','398','256',
                         '296','259','368','638','396','238','356','659','639','666','359','336','299',
                         '338','696','269','358','656','698','699','298','236','239'])]

        for e in expectations:
            self.assertEqual(sorted(get_pins(e[0])), sorted(e[1]), "PIN: " + e[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
