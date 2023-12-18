class Solution:
    def compress(self, chars: List[str]) -> int:
        # alternative array solution:
        # ret = []
        # count = 1

        # for c1, c2 in zip(chars, chars[1:] + [None]):
        #     if c1 != c2:
        #         ret.append(c1)
        #         if count > 1:
        #             ret += list(str(count))
        #         count = 1
        #     else:
        #         count += 1
        
        # # required in-place operation
        # chars.clear()
        # for c in ret:
        #     chars.append(c)
        
        # return len(chars)

        # real in-place solution
        offset, counter = 0, 1
        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                chars[offset] = chars[i - 1]
                offset += 1
                if counter > 1:
                    for n in list(str(counter)):
                        chars[offset] = n
                        offset += 1
                counter = 1
            else:
                counter += 1
        else:
            chars[offset] = chars[-1]
            offset += 1
            if counter > 1:
                for n in list(str(counter)):
                    chars[offset] = n
                    offset += 1
        del chars[offset:]
        return len(chars)
