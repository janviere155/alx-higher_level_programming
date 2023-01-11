#!/usr/bin/python3
"""Module to create a function for pascal's triangle"""


def pascal_triangle(n):
    """Tabulate the triangle"""
    tri = []
    prev = None
    if n <= 0:
        return []
    else:
        for a in range(n):
            row = []
            j = 0
            while j <= a:
                if j == 0 or j == a:
                    row.append(1)
                else:
                    row.append(prev[j - 1] + prev[j])
                j += 1
            prev = row.copy()
            tri.append(row)
    return tri
