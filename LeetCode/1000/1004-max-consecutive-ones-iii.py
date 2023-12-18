class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # # two pointers solution:
        # lhs = rhs = 0
        # while rhs < len(nums) and (nums[rhs] == 1 or k > 0):
        #     if nums[rhs] == 0:
        #         k -= 1
        #     rhs += 1
        
        # if rhs == len(nums):
        #     return len(nums)
        
        # max_ones = rhs - lhs
        # while rhs < len(nums):
        #     rhs += 1

        #     # relocate flips; move lhs
        #     if nums[rhs - 1] == 0:
        #         while lhs < rhs and nums[lhs] == 1:
        #             lhs += 1
        #         lhs += 1
            
        #     max_ones = max(max_ones, rhs - lhs)
        
        # return max_ones

        # keep or expand solution:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            print(l, r)
        return r-l+1