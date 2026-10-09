class Solution:
    """
    Brute Force

    Remember a rule of thumb in backtracking where if you appended
    an element in a shared list, always remove it or pop it
    after the function call so that the parent's list won't get
    corrupted.

    Time Complexity: O(n * 2^(2n))
    Space Complexity: O(n * 2^(2n))
    """

    """
    Time Complexity: O(n * 2^(2n)) + O(2^(2n) * 2n) = O(n * 2^(2n))
    Space Complexity: O(2^(2n) + m)
    m is the length of `all_valid_parenthesis_strings`.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        all_parenthesis_strings = []
        self.generateParenthesisHelper(n, [], all_parenthesis_strings)
        all_valid_parenthesis_strings = []

        for parenthesis_string in all_parenthesis_strings:
            counter = 0

            for parenthesis in parenthesis_string:
                if counter < 0:
                    break
                elif parenthesis == "(":
                    counter += 1
                else:
                    counter -= 1
            
            if counter == 0:
                all_valid_parenthesis_strings.append(parenthesis_string)

        return all_valid_parenthesis_strings

    """
    Time Complexity: O(n * 2^(2n))
    Space Complexity: O(n * 2^(2n))
    """
    def generateParenthesisHelper(
        self, 
        n: int, 
        current_parenthesis_string: List[str], 
        all_parenthesis_strings: List[List[str]]
    ) -> None:
        if len(current_parenthesis_string) == n * 2:
            all_parenthesis_strings.append("".join(current_parenthesis_string))

            return

        current_parenthesis_string.append("(")
        self.generateParenthesisHelper(n, current_parenthesis_string, all_parenthesis_strings)
        current_parenthesis_string.pop()
        current_parenthesis_string.append(")")
        self.generateParenthesisHelper(n, current_parenthesis_string, all_parenthesis_strings)
        current_parenthesis_string.pop()