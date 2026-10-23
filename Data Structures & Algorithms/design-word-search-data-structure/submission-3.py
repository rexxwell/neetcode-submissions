import re

class WordDictionary:
    """
    Brute Force

    Runtime: 1092ms (TLE)
    Memory: 12.2 MB (TLE)
    Time Complexity: O(n * m * o)
    Space Complexity: O(n)
    n is the length of `self.words`.
    m is the length of `word`.
    o is the length of `existing_word`.
    """

    """
    Time Complexity: O(1)
    Space Complexity: O(n)
    n is the length of `self.words`.
    """
    def __init__(self):
        self.words = set()

    """
    Time Complexity: O(1) average
    Space Complexity: O(1)
    """
    def addWord(self, word: str) -> None:
        self.words.add(word)

    """
    Time Complexity: O(n * m * o)
    Space Complexity: O(1)
    n is the length of `self.words`.
    m is the length of `word`.
    o is the length of `existing_word`.
    """
    def search(self, word: str) -> bool:
        for existing_word in self.words:
            if re.fullmatch(word, existing_word):
                return True

        return False
