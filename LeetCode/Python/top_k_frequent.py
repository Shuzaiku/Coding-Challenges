class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pointers = {}
        for num in nums:
            if not num in pointers:
                pointers[num] = 1
            else:
                pointers[num] += 1
        
        frequents = [None] * k
        for i in range(k):
            for key, val in pointers.items():
                curr_num = frequents[i]
                if curr_num == None or pointers[curr_num] < val:
                    frequents[i] = key
            pointers.pop(frequents[i])
        return frequents
