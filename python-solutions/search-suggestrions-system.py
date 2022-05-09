from typing import List


class TrieNode:
    def __init__(self):
        # 26 lower case letters in the alphabet
        self.children = [None]*26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word: str):
        currentNode = self.root
        for char in word:
            # for ordering control
            i = ord(char) - ord("a")
            if currentNode.children[i]:
                currentNode = currentNode.children[i]
            else:
                return None
        return currentNode

    def insert(self, word: str):
        currentNode = self.root
        for char in word:
            # for ordering control
            i = ord(char) - ord("a")
            if currentNode.children[i] is None:
                currentNode.children[i] = TrieNode()
            currentNode = currentNode.children[i]
            # Mark the end of a work with an asterisk
        currentNode.isWord = True

    def collectTopThreeWords(self, node, prefix="", words=[]):
        if (len(words) == 3):
            return
        if node.isWord:
            words.append(prefix)
        for i in range(26):
            if node.children[i]:
                self.collectTopThreeWords(
                    node.children[i], prefix + chr(ord("a") + i), words)

    def lexicographicalMinimums(self, prefix: str):
        currentNode = self.search(prefix)
        words = []
        if not currentNode:
            return words
        self.collectTopThreeWords(currentNode, prefix, words)
        return words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = buildTrie(products)
        result = []
        for i in range(len(searchWord)):
            result.append(root.lexicographicalMinimums(searchWord[:i+1]))
        return result


def buildTrie(products: List[str]) -> Trie:
    root = Trie()
    for product in products:
        root.insert(product)
    return root
