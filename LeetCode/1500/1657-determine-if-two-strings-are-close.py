class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        set1, set2 = set(word1), set(word2)
        if not set1 == set2:
            return False

        from collections import Counter
        c1 = sorted(list(Counter(word1).values()))
        c2 = sorted(list(Counter(word2).values()))

        return c1 == c2