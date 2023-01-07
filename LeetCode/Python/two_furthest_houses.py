class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        low_houses = {}
        high_houses = {} # these dictionaries will hold (k,v) as (color,idx)
        
        for i, color in enumerate(colors):
            if not color in low_houses:
                low_houses[color] = i
                high_houses[color] = i
            else:
                high_houses[color] = i
                
        biggest_dist = 0
        for l_house, i in low_houses.items():
            for h_house, j in high_houses.items():
                if l_house == h_house:
                    continue
                
                dist = j-i
                if biggest_dist < dist:
                    biggest_dist = dist
        return biggest_dist
