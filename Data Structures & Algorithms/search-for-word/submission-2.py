class Solution:
    """
    Backtracking

    Runtime: 45ms
    Memory: 8.0 MB
    Time Complexity: O(n * m * 4^l)
    Space Complexity: O(l)
    n is the number of rows in `board`.
    m is the number of columns in each row in `board`.
    l is the length of `word`.
    """

    """
    Time Complexity: O(n * m * 4^l)
    Space Complexity: O(1)
    n is the number of rows in `board`.
    m is the number of columns in each row in `board`.
    l is the length of `word`.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        for row in range(len(board)):
            for column in range(len(board[row])):
                if self.existHelper(board, word, row, column, 0, set()):
                    return True

        return False

    """
    Time Complexity: O(4^l)
    Space Complexity: O(l)
    l is the length of `word`.
    """
    def existHelper(
        self, 
        board: List[List[str]], 
        word: str,
        row: int,
        column: int,
        i: int,
        visited: set[tuple[int, int]]
    ) -> bool:
        if (
            (row < 0 or row >= len(board)) or
            (column < 0 or column >= len(board[row])) or
            (board[row][column] != word[i]) or
            ((row, column) in visited)
        ):
            return False

        if i == len(word) - 1:
            if board[row][column] == word[i]:
                return True

        visited.add((row, column))
        result = (
            self.existHelper(board, word, row - 1, column, i + 1, visited) or
            self.existHelper(board, word, row, column + 1, i + 1, visited) or
            self.existHelper(board, word, row + 1, column, i + 1, visited) or
            self.existHelper(board, word, row, column - 1, i + 1, visited)
        )
        visited.remove((row, column))

        return result