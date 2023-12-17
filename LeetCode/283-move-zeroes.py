class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # naive swapping solution:
        # i = len(nums) - 1
        # while i > 0:
        #     for j in range(i):
        #         if nums[j] == 0:
        #             for k in range(j, i):
        #                 nums[k], nums[k+1] = nums[k+1], nums[k]
        #             continue
        #     i -= 1
        
        # # del and insert solution:
        # to_del = [i for i, n in enumerate(nums) if n == 0]
        # for i in to_del[::-1]:
        #     del nums[i]
        #     nums.append(0)

        # # two pointers solution:
        # lhs = 0
        # for rhs in range(len(nums)):
        #     if nums[rhs] != 0:
        #         nums[lhs], nums[rhs] = nums[rhs], nums[lhs]
        #         lhs += 1

        # move non-zero forward and fill by zeros:
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1