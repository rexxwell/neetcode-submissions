class Solution:
    """
    Backtracking

    For a given string, we have 2^n possible partitions because at every index in
    `s`, we are given two choices:

    1. Partition the string at this index.
    2. Continue the string at this index.

    Runtime: 1093ms (TLE)
    Memory: 9.1 MB (TLE)
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n)
    n is the length of `s`.
    """

    """
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n)
    n is the length of `s`.
    """
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        palindromic_substrings = []
        self.partitionHelper(s, palindromic_substrings, [], 0, 1)

        return palindromic_substrings

    """
    Time Complexity: O(2^n * n)
    Space Complexity: O(n)
    n is the length of `s`.
    """
    def partitionHelper(self, s: str, palindromic_substrings: List[List[str]], current_substrings: List[str], i: int, j: int) -> None:
        if j == len(s):
            if self.isPalindrome(s[i:j]):
                current_substrings.append(s[i:j])
                palindromic_substrings.append(current_substrings.copy())
                current_substrings.pop()

            return
        
        if self.isPalindrome(s[i:j]):
            current_substrings.append(s[i:j])
            self.partitionHelper(s, palindromic_substrings, current_substrings, j, j + 1)
            current_substrings.pop()
            
        self.partitionHelper(s, palindromic_substrings, current_substrings, i, j + 1)

    """
    Time Complexity: O(o)
    Space Complexity: O(1)
    o is the length of `substring`.
    """
    def isPalindrome(self, substring: str) -> bool:
        if not substring:
            return False

        i = 0
        j = len(substring) - 1

        while i < j:
            if substring[i] != substring[j]:
                return False
            
            i += 1
            j -= 1
        
        return True