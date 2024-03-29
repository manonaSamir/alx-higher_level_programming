#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        prev = triangles[-1]
        temp = [1]
        for i in range(len(prev) - 1):
            temp.append(prev[i] + prev[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
