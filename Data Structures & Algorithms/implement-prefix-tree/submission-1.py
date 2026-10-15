class PrefixTree:
    """
    Brute Force

    Runtime: 1094ms
    Memory: 14.5 MB
    Time Complexity: O(nm)
    Space Complexity: O(n)
    n is the length of `self.strings`.
    m is the length of `string`.
    """

    """
    Time Complexity: O(1)
    Space Complexity: O(n)
    n is the length of `self.strings`.
    """
    def __init__(self):
        self.strings = set()

    """
    Time Complexity: O(1) average
    Space Complexity: O(1)
    """
    def insert(self, word: str) -> None:
        self.strings.add(word)

    """
    Time Complexity: O(1) average
    Space Complexity: O(1)
    """
    def search(self, word: str) -> bool:
        return word in self.strings

    """
    Time Complexity: O(nm)
    Space Complexity: O(1)
    n is the length of `self.strings`.
    m is the length of `string`.
    """
    def startsWith(self, prefix: str) -> bool:
        for string in self.strings:
            if prefix in string:
                return True
        
        return False