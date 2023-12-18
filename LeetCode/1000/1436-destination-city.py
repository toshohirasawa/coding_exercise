class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # naive solution:
        from_cities = set([p[0] for p in paths])
        to_cities = set([p[1] for p in paths])

        return (to_cities - from_cities).pop()

        # for city in to_cities:
        #     if city not in from_cities:
        #         return city
        
        # return None
        