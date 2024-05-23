#!/usr/bin/env python3
"""
    A function def determinant(matrix):
    that calculates the determinant of a matrix:
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix

    Args:
        - matrix: list of lists whose determinant

    Returns:
        - the determinant of matrix

    """
    # Check if the input is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square
    num_rows = len(matrix)
    if num_rows != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Base case: 0x0 matrix has determinant 1
    if num_rows == 0:
        return 1

    # Base case: 1x1 matrix has determinant equal to its element
    if num_rows == 1:
        return matrix[0][0]

    det = 0
    for col in range(num_rows):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += (-1) ** col * matrix[0][col] * determinant(minor)

    return det
