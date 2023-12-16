class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empties = 1
        n_can_plant = 0

        for s in flowerbed:
            if s == 0:
                empties += 1
            else:
                n_can_plant += max((empties - 1), 0) // 2
                empties = 0
        else:
            n_can_plant += empties // 2
        
        return n_can_plant >= n