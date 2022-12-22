class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        reps = {}

        for num in nums:
            reps[num] = reps.get(num, 0) + 1
        for num, rep in reps.items():
            if rep == n:
                return num
