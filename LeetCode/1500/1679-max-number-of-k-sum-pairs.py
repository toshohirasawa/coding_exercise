class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # # naive solution:
        # counter = 0
        # while len(nums) > 0:
        #     removed = False
        #     for i in range(len(nums)):
        #         for j in range(i+1, len(nums)):
        #             if nums[i] + nums[j] == k:
        #                 counter += 1
        #                 del nums[j]
        #                 del nums[i]
        #                 removed = True
        #                 break
        #         if removed:
        #             break
        #     if not removed:
        #         break
        # return counter

        # mid = k//2
        # num_indexes = [[0, 0] for _ in range(mid)]

        # for i, n in enumerate(nums):
        #     if n <= k//2:
        #         num_indexes[n-1][0] += 1
        #     elif n < k:
        #         num_indexes[k-n-1][1] += 1

        # if k % 2 == 0:
        #     lhs = num_indexes[mid-1][0] // 2
        #     rhs = num_indexes[mid-1][0] - lhs
        #     num_indexes[mid-1] = [lhs, rhs]

        # # print(num_indexes)

        # counter = 0
        # for n1, n2 in num_indexes:
        #     counter += min(n1, n2)
        
        # return counter

        # sort and pointer solution:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1

        counter = 0
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                counter += 1
                i += 1
                j -= 1
            elif s > k:
                j -= 1
            else:
                i += 1

        return counter
