#!/usr/bin/env python3


def longest_common_subsequence(a, b):
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    """
    Example matrix w/ len(a) == 3 and len(b) == 6 and zero padding around borders:

    [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]
    """

    # Add padding to string a and b so we do not have to offset matrix index corresponding
    # to the index of the string

    a = "0" + a
    b = "0" + b

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    i, j = len(a) - 1, len(b) - 1

    lcs = ""

    while i > 0 and j > 0:
        if a[i] == b[j]:
            lcs = a[i] + lcs
            i, j = i - 1, j - 1
        else:
            if matrix[i-1][j] >= matrix[i][j-1]:
                i = i - 1
            else:
                j = j - 1


    return lcs, len(lcs)

lcs = longest_common_subsequence('foo', 'fboaro')

print(lcs)

