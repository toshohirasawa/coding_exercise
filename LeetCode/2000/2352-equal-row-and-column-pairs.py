class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # # naive solution:
        # n_ans = 0
        # for i in range(n):
        #     for j in range(n):
        #         row = grid[i]
        #         col = [r[j] for r in grid]
        #         if row == col:
        #             n_ans += 1
        
        # return n_ans
        
        # rows, cols = defaultdict(int), defaultdict(int)
        # for i in range(n):
        #     rows[str(grid[i])] += 1
        #     cols[str([r[i] for r in grid])] += 1
        
        # n_ans = 0
        # for v in (set(rows.keys()) & set(cols.keys())):
        #     n_ans += rows[v] * cols[v]
        
        # return n_ans

        rows = Counter(map(tuple,grid))
        cols = Counter(zip(*grid))
        return sum(rows[i]*cols[i] for i in rows)