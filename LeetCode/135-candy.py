class Solution:
    def candy(self, ratings: List[int]) -> int:
        # initialization
        candies_left = [1 for _ in ratings]
        candies_right = [1 for _ in ratings]

        for i, (r1, r2) in enumerate(zip([2*10**4+1]+ratings, ratings)):
            if r2 > r1:
                candies_left[i] = candies_left[i-1] + 1
        for i, (r2, r3) in list(enumerate(zip(ratings, ratings[1:]+[2*10**4+1])))[::-1]:
            if r2 > r3:
                candies_right[i] = candies_right[i+1] + 1

        candies = [max(l,r) for l, r in zip(candies_left, candies_right)]

        # update
        updated = True
        while updated:
            updated = False

            for i, (r1, r2, r3) in enumerate(zip(
                [2*10**4+1] + ratings,
                ratings,
                ratings[1:] + [2*10**4+1]
            )):
                new_candy = candies[i]
                
                if r2 > r1:
                    new_candy = max(candies[i-1] + 1, new_candy)
                if r2 > r3:
                    new_candy = max(candies[i+1] + 1, new_candy)
                
                if candies[i] != new_candy:
                    candies[i] = new_candy
                    updated = True

        return sum(candies)
            
            