class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # # naive solution:
        # max_total = sum(nums[:k])
        # for b in range(1, n - k + 1):
        #     total = sum(nums[b:b+k])
        #     if total > max_total:
        #         max_total = total
        # return max_total / k

        # moving indicator solution:
        total = max_total = sum(nums[:k])
        for i in range(k, n):
            total += nums[i] - nums[i-k]
            max_total = max(total, max_total)
        return max_total / k