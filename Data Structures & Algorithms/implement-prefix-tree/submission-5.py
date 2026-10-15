class PrefixTree:
    """
    Brute Force

    Runtime: 124ms
    Memory: 15.1 MB
    Time Complexity: O(m)
    Space Complexity: O(n)
    m is the length of `word`.
    n is the length of `self.strings`.
    """

    """
    Time Complexity: O(1)
    Space Complexity: O(n)
    n is the length of `self.strings`.
    """
    def __init__(self):
        self.strings = set()
        self.prefixes = set()

    """
    Time Complexity: O(m)
    Space Complexity: O(1)
    m is the length of `word`.
    """
    def insert(self, word: str) -> None:
        self.strings.add(word)

        for i in range(1, len(word)):
            self.prefixes.add(word[0:i])

    """
    Time Complexity: O(1) average
    Space Complexity: O(1)
    """
    def search(self, word: str) -> bool:
        return word in self.strings

    """
    Time Complexity: O(1) average
    Space Complexity: O(1)
    n is the length of `self.strings`.
    m is the length of `string`.
    """
    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes or prefix in self.strings