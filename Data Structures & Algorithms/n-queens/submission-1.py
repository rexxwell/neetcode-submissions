class Solution:
    """
    Backtracking

    If we looped through every single spot and recursively found a spot where
    the queen does not attack each other, that would lead to a Time Limit
    Exceeded error. So, use the key insights below:

    - Since no two queens can share the same row, every single row must contain exactly one queen.
    
    This means that we don't have to search the entire board or maintain a separate queen
    counter. We just have to pass the row index where we loop through
    each row index and then we decide where to put this queen in this row.
    Inside the helper function, you would loop through the columns,
    if `(row, col)` is a valid spot, then place the queen, call `backtrack(row + 1)`,
    then remove the queen (backtrack).

    If we want to check if a spot is safe, we just have to make sure
    that the queen being placed is not in the same column that was used before.
    The row is already accounted for since we are already looping through each
    row. For diagonals, notice that for any diagonals, `row + col` is a constant
    for positive diagonals and `row - col` is a constant for negative diagonals.
    Thus, we would need to have 3 sets to hold this information.

    Runtime: 162ms
    Memory: 10.6 MB
    Time Complexity: O(n!)
    Space Complexity: O(n^2)
    `current_solution` holds n List with n strings inside, n^2.
    """

    """
    Time Complexity: O(n!)
    Space Complexity: O(m) in total, O(1) auxilliary space
    m is the length of `distinct_solutions`.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        
        distinct_solutions = []
        self.solveNQueensHelper(
            n,
            distinct_solutions,
            [["."] * n for _ in range(n)],
            set(),
            set(),
            set(),
            0
        )

        return distinct_solutions

    """
    Time Complexity: O(n!)
    Space Complexity: O(n^2 + n + l + o + p) = O(n^2)
    `current_solution` holds n List with n strings inside, n^2.
    l is the length of `columns_used`.
    o is the length of `positive_diagonals_used`.
    p is the length of `negative_diagonals_used`.
    The deepest recursion depth of this helper function would be
    O(n) since the base case stops at n.
    """
    def solveNQueensHelper(
        self,
        n: int, 
        distinct_solutions: List[List[str]], 
        current_solution: List[List[str]],
        columns_used: set(int),
        positive_diagonals_used: set(int),
        negative_diagonals_used: set(int),
        current_row: int
    ) -> None:
        if current_row == n:
            distinct_solutions.append(["".join(row) for row in current_solution])

            return

        for column in range(n):
            if (
                column not in columns_used and
                (current_row + column) not in positive_diagonals_used and
                (current_row - column) not in negative_diagonals_used
            ):
                current_solution[current_row][column] = "Q"
                columns_used.add(column)
                positive_diagonals_used.add(current_row + column)
                negative_diagonals_used.add(current_row - column)
                self.solveNQueensHelper(
                    n,
                    distinct_solutions,
                    current_solution,
                    columns_used,
                    positive_diagonals_used,
                    negative_diagonals_used,
                    current_row + 1
                )
                current_solution[current_row][column] = "."
                columns_used.remove(column)
                positive_diagonals_used.remove(current_row + column)
                negative_diagonals_used.remove(current_row - column)