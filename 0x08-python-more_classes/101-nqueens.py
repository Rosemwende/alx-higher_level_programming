#!/usr/bin/python3
"""N Queens problem."""


import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    """A recursive utility function to solve N Queens problem."""
    # Base case: If all queens are placed, then return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column col, then return False
    return False


def solve_n_queens(n):
    """Solve the N Queens problem."""
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Check if a solution exists
    if not solve_n_queens_util(board, 0, n):
        return None

    # Convert the board to the required format
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if board[i][j] == 1:
                row.append([i, j])
        result.append(row)

    return result


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_n_queens(n)

    # Print the solutions
    if solutions:
        for sol in solutions:
            print(sol)
    else:
        print("No solution found")
