class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counters = [arr.count(i) for i in set(arr)]
        return len(set(counters)) == len(counters)