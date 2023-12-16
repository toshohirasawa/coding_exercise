class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product_all(arr):
            ret = 1
            for item in arr:
                ret *= item
            return ret
        
        p = product_all(nums)
        return [
            p//n if n != 0 else product_all(nums[:i]) * product_all(nums[i+1:]) 
            for i, n in enumerate(nums)
        ]
