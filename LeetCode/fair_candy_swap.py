class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        equal_size = (alice_total + bob_total) // 2
        
        bob_set = set(bobSizes)
        for alice_candies in aliceSizes:
            bob_swap = equal_size - (alice_total - alice_candies) 
            if bob_swap in bob_set:
                return [alice_candies, bob_swap]
