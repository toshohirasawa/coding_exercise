class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def iter_factors(n):
            for i in range(1, n+1):
                if n % i == 0:
                    yield i

        def iter_candidates(s):
            for i in list(iter_factors(len(s)))[::-1]:
                yield s[:i]

        def is_divided_by(s1, s2):
            if len(s1) % len(s2) != 0:
                return False
            
            return s1 == (s2 * (len(s1) // len(s2)))

        for cand in iter_candidates(str1 if l1 < l2 else str2):
            if is_divided_by(str1, cand) and is_divided_by(str2, cand):
                return cand
        
        return ""