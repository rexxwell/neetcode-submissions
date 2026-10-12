class Solution:
    """
    Backtracking

    Runtime: 28ms
    Memory: 8.0 MB
    Time Complexity: O(n * ∏k_i) = O(n * 4^n)
    Space Complexity: O(n * ∏k_i) = O(n * 4^n) total, O(n) auxilliary
    n is the length of `digits`.
    k_i is the number of characters mapped to d_i where d_i
    is the ith digit in `digits`, where i = 0...n.
    """

    mapped_characters_by_digits = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    """
    Time Complexity: O(n * ∏k_i) = O(n * 4^n)
    Space Complexity: O(n * ∏k_i) = O(n * 4^n) total, O(n) auxilliary
    n is the length of `digits`.
    k_i is the number of characters mapped to d_i where d_i
    is the ith digit in `digits`, where i = 0...n.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letter_combinations = []
        self.letterCombinationsHelper(
            digits, 
            letter_combinations, 
            "", 
            0
        )

        return letter_combinations

    """
    Time Complexity: O(n * ∏k_i) = O(n * 4^n)
    Space Complexity: O(n)
    n is the length of `digits`.
    k_i is the number of characters mapped to d_i where d_i
    is the ith digit in `digits`, where i = 0...n.
    """
    def letterCombinationsHelper(
        self, 
        digits: str,
        letter_combinations: List[str],
        current_letter_combination: str,
        i: int
    ) -> None:
        if len(current_letter_combination) == len(digits):
            letter_combinations.append(current_letter_combination)
            
            return
        
        if i >= len(digits):
            return

        for character in self.mapped_characters_by_digits[digits[i]]:
            self.letterCombinationsHelper(
                digits,
                letter_combinations,
                current_letter_combination + character,
                i + 1
            )