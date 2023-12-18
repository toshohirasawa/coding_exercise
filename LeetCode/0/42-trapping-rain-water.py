class Solution:
    def trap(self, height: List[int]) -> int:
        depth = []

        current_h = 0
        for h in height:
            if h < current_h:
                depth.append(current_h - h)
            else:
                depth.append(0)
                if h > current_h:
                    current_h = h
        
        current_h = 0
        for i, h in list(enumerate(height))[::-1]:
            if h < current_h:
                depth[i] = min(depth[i], current_h - h)
            else:
                depth[i] = 0
                if h > current_h:
                    current_h = h
        
        return sum(depth)
