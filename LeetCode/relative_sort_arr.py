class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for n in arr2:
            order[n] = 0
            
        
        not_included = []
        for n in arr1:
            if n in order:
                order[n] += 1
            else:
                not_included.append(n)
        not_included.sort()
            
        new_arr = []
        for n in arr2:
            for _ in range(order[n]):
                new_arr.append(n)
        return new_arr + not_included
