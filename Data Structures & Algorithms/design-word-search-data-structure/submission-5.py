import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    """
    Trie

    Runtime: 150ms
    Memory: 14.4 MB
    Time Complexity: 
        Best Case: O(n)
        Worst Case: O(26^n)
    Space Complexity: O(n)
    n is the length of `word`.
    """

    """
    Time Complexity: O(1) 
    Space Complexity: O(1)
    """
    def __init__(self):
        self.root = TrieNode()

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    n is the length of `word`.
    """
    def addWord(self, word: str) -> None:
        curr = self.root

        for character in word:
            if character not in curr.children:
                curr.children[character] = TrieNode()
            
            curr = curr.children[character]

        curr.is_end_of_word = True

    """
    Time Complexity:
        Best Case: O(n)
        Worst Case: O(26^n)
    Space Complexity: O(n) 
    n is the length of `word`.
    """
    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word, 0);

    """
    Time Complexity:
        Best Case: O(n)
        Worst Case: O(26^n)
    Space Complexity: O(n)
    n is the length of `word`.
    """  
    def searchHelper(self, curr: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return curr.is_end_of_word
        
        if word[index] == ".":
            for child in curr.children:
                if self.searchHelper(curr.children[child], word, index + 1):
                    return True
            
            return False
        else:
            if word[index] in curr.children:
                return self.searchHelper(curr.children[word[index]], word, index + 1)
            else:
                return False
