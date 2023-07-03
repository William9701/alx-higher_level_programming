#!/usr/bin/python3
""" This is a queen code"""


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Returns:
        None

    """
    def is_safe(board, row, col):
        """
        Check if placing a queen at the current position (row, col)
        is safe and does not attack any other queens.

        Args:
            board (List[int]): The current board configuration.
            row (int): The current row to check.
            col (int): The current column to check.

        Returns:
            bool: True if the position is safe, False otherwise.

        """
        for i in range(row):
            if (
                board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row
            ):
                return False
        return True

    def solve(board, row, result):
        """
        Recursively solve the N-Queens problem using backtracking.

        Args:
            board (List[int]): The current board configuration.
            row (int): The current row to consider.
            result (List[List[int]]): A list to store the solutions.

        Returns:
            None

        """
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
        """
        Print all the solutions to the N-Queens problem.

        Args:
            result (List[List[int]]): A list of solutions.

        Returns:
            None

        """
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
