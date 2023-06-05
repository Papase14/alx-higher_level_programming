#!/usr/bin/python3
"""
    nqueens backtracking program to print the coordinates of n queens
    on an nxn grid such that they are all in non-attacking positions
"""

import sys

def n_queens(n):
    # check if n is an integer 
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    # check if n is greater or equal to 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # create a board of size n x n
    board = [[0] * n for i in range(n)]

    # place the queens
    place_queen(board, 0, n)

def place_queen(board, row, n):
    # check if all queens are placed
    if row == n:
        print_solution(board, n)
        return True

    # place queen in each column of the current row
    for col in range(n):
        # check if the queen can be placed
        if is_safe(board, row, col, n):
            # place the queen
            board[row][col] = 1

            # place the remaining queens
            if place_queen(board, row + 1, n):
                return True

            # backtrack
            board[row][col] = 0

    return False

def is_safe(board, row, col, n):
    # check if the queen can be placed in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("q", end=" ")
            else:
                print("-", end=" ")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    n_queens(n)
