class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def iter_chr(w, max_len):
            empties = max(0, max_len - len(w))
            for c in w:
                yield c
            for _ in range(empties):
                yield ''
        
        wlen = max(len(word1), len(word2))

        return ''.join([
            c1+c2 for c1, c2 in zip(iter_chr(word1, wlen), iter_chr(word2, wlen))
        ])