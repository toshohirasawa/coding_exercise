class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i, lhs, rhs =0,  0, sum(nums[1:])
        while lhs != rhs:
            i += 1
            if i >= len(nums):
                return -1
            lhs += nums[i-1]
            rhs -= nums[i]
        return i