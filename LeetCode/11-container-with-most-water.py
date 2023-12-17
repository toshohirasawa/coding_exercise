class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        # # naive solution:
        # waters = [
        #     max([min(height[i], height[j]) * (j-i) for j in range(i+1, n)])
        #     for i in range(n-1)
        # ]
        # return max(waters)

        # # window-based solution:
        # window = n - 1
        # max_area = 0
        # while window > 0:
        #     max_height = 0
        #     for i in range(n - window):
        #         a_height = min(height[i], height[i+window])
        #         if a_height > max_height:
        #             max_height = a_height
        #     area = max_height * window
        #     if area > max_area:
        #         max_area = area
            
        #     window -= 1

        # return max_area

        # pointer-based solution:
        i, j, max_area = 0, n - 1, 0
        while i < j:

            a_height = min(height[i], height[j])
            area = a_height * (j - i)
            if area > max_area:
                max_area = area

            # move pointer
            if a_height == height[i]:
                i += 1
            else:
                j -= 1
        
        return max_area
                

