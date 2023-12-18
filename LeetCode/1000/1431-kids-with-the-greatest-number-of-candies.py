class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # naive solution
        max_candies = max(candies)

        return [c + extraCandies >= max_candies for c in candies]
