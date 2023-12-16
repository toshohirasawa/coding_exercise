from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # initial plan
        lines = [[]]
        for w in words:
            if sum(len(_w) + 1 for _w in lines[-1]) + len(w) >maxWidth:
                lines.append([])
            
            lines[-1].append(w)
        
        # spacing
        out_strs = []
        for line in lines[:-1]:
            n_spaces = maxWidth - sum(len(w) for w in line)
            n_slots = len(line) - 1
            if n_slots == 0:
                out_str = line[0].ljust(maxWidth, ' ')
            else:
                each_spaces = [' ' * (n_spaces // (n_slots)) for _ in range(n_slots)]
                if n_spaces % n_slots != 0:
                    for i in range(n_spaces % n_slots):
                        each_spaces[i] = each_spaces[i] + ' '
            
                out_str = ''
                for w, spaces in zip(line, each_spaces + ['']):
                    out_str += w + spaces
            
            out_strs.append(out_str)

        out_strs.append(' '.join(lines[-1]).ljust(maxWidth, ' '))
        
        return out_strs
