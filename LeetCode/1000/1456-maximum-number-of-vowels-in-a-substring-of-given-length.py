class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c, vowels = 'aeiou'):
            return 1 if c in vowels else 0
        
        total = max_total = sum([is_vowel(c) for c in s[:k]])

        for i in range(k, len(s)):
            total += is_vowel(s[i]) - is_vowel(s[i-k])
            max_total = max(total, max_total)
        
        return max_total