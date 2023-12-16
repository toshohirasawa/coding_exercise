class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i, c in enumerate(s) if c.lower() in ['a','e','i','o','u']]
        s = list(s)

        for x, y in zip(vowels[:len(vowels)//2], vowels[::-1][:len(vowels)//2]):
            s[x], s[y] = s[y], s[x]
        
        return ''.join(s)