from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # O(n^2) solution
        # num_nums = len(nums)
        # for i in range(num_nums):
        #     for j in range(i+1, num_nums)[::-1]:
        #         n1, n2 = nums[i], nums[j]
        #         if n1 + n2 == target:
        #             return i, j
        # return -1, -1

        # O(n * log(n)) solution: binary search solution
        def binary_search(arr, l, r, x):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        snums, n = sorted(nums), len(nums)
        for i in range(n):
            complement = target - snums[i]
            found = binary_search(snums, i+1, n-1, complement)

            if found != -1:
                n1, n2 = snums[i], snums[found]
                # forward and backward search to avoid index collision
                return nums.index(n1), n - nums[::-1].index(n2) - 1
        
        return -1, -1