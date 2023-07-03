#!/usr/bin/python3
def solve_nqueens(N):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def solve(board, row, result):
        if row == N:
            solution = [[r, c] for r, c in enumerate(board)]
            result.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1, result)
                board[row] = -1

    def print_solutions(result):
        for solution in result:
            print(solution)
        print()

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * N
    solutions = []
    solve(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = sys.argv[1]
    solve_nqueens(N)

