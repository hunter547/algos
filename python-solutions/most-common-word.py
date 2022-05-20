from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        only_words = ''.join(
            [c.lower() if c.isalnum() else ' ' for c in paragraph]).split()
        banned_words = set(banned)
        word_count = defaultdict(int)
        for word in only_words:
            if word not in banned_words:
                word_count[word] += 1
        return max(word_count, key=word_count.get)
