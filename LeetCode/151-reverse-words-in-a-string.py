class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w for w in [word for word in s.split(' ')] if len(w) > 0]

        return ' '.join(words[::-1])