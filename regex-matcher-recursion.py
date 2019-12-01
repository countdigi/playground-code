#!/usr/bin/env python3

import unittest


def match(text, pattern):
    if DEBUG:
        print(f"match() text:{text} pattern:{pattern}")

    ## if pattern is done the return true if text is done - otherwise false
    if not pattern:
        return not text

    if text and (pattern[0] == text[0] or pattern[0] == "."):
        matches = True
    else:
        matches = False # <--- z != a

    if len(pattern) >= 2 and pattern[1] == '*':
        return ((match(text, pattern[2:])) or
                matches and match(text[1:], pattern))
                # s= p=a*b
    else:
        return matches and match(text[1:], pattern[1:])


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(match("abcd", "z*a*bcd"), True)

if __name__ == "__main__":
    DEBUG = False
    unittest.main()
