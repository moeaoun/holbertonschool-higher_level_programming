#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        # Check if there's a queen in the same column or diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row):
    """Solve the N queens problem using backtracking."""
    if row == N:
        # A solution has been found, print it
        print([[i, board[i]] for i in range(N)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Place the queen
            solve_nqueens(N, board, row + 1)  # Recur to place the next queen
            # No need to backtrack as we only place one queen per row

def nqueens(N):
    """Solves the N queens puzzle and prints all possible solutions."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board
    board = [-1] * N
    solve_nqueens(N, board, 0)

def main():
    """Main function to handle command line input."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)

if __name__ == "__main__":
    main()

