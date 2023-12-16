class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # # compress array
        # _nums = nums[:1]
        # for n in nums[1:]:
        #     if _nums[-1] != n:
        #         _nums.append(n)
        # nums = _nums

        # assertion
        if len(nums) < 3:
            return False
            
        # # naive solution:
        # # TLE
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True        
        # return False

        # # # improved solution:
        # uniq_nums = sorted(list(set(nums)))
        # num_ids = [[] for _ in uniq_nums]
        # for i, n in enumerate(nums):
        #     num_ids[uniq_nums.index(n)].append(i)

        # for k in range(len(uniq_nums))[::-1]:
        #     k_cands = num_ids[k]
        #     k_max = max(k_cands)
        #     for j in range(len(uniq_nums[:k]))[::-1]:
        #         j_cands = [idx for idx in num_ids[j] if idx < k_max]
        #         if len(j_cands) == 0:
        #             continue

        #         j_max = max(j_cands)
        #         for i in range(len(uniq_nums[:j][::-1])):
        #             i_cands = [idx for idx in num_ids[i] if idx < j_max]
        #             if len(i_cands) > 0:
        #                 return True
        # return False

        # improved solution 2:
        tgt = max(nums[:2]) + 1 if nums[0] < nums[1] else None
        n_i = min(nums[:2])

        for n in nums[2:]:
            if tgt is not None and n >= tgt:
                return True

            # determine update tgt 
            if tgt is None or n < tgt -1:
                if n_i < n:
                    tgt = n + 1
                else:
                    if n < n_i:
                        n_i = n
                
                print(tgt, n_i)
            
        return False

        # # solution by hiepit:
        # first = second = math.inf
        # for num in nums:
        #     if num <= first:
        #         first = num
        #     elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
        #         second = num
        #     else:  # Now first < second < num
        #         return True
        # return False
    