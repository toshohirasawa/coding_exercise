class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # # naive solution:
        # n = len(words[0])
        # window = n * len(words)

        # def is_matched(subs):
        #     used = set()
        #     for i in range(len(words)):
        #         ss = subs[i*n:(i+1)*n]
        #         if ss not in words:
        #             return False
        #         else:
        #             for j, w in enumerate(words):
        #                 if ss == w and j not in used:
        #                     used.add(j)
        #                     break
        #             else:
        #                 return False
        #     return True

        # matches = []
        # for i in range(len(s)):
        #     if is_matched(s[i:i+window]):
        #         matches.append(i)

        # return matches
        
        # count-down solution:
        n, m = len(words), len(words[0])
        matches = []
        for offset in range(m):
            ss = s[offset:]
            counter = {
                w: words.count(w)
                for w in set(words)
            }
            for i in range(0, len(ss)//m):
                add = ss[i*m:(i+1)*m]
                remove = ss[(i-n)*m:(i-n+1)*m] if i>=n else None
                if add in counter:
                    counter[add] -= 1
                if remove:
                    if remove in counter:
                        counter[remove] += 1
                # print(add, remove, counter)
                if all([v == 0 for v in counter.values()]):
                    matches.append((i-n+1)*m+offset)
        return matches

