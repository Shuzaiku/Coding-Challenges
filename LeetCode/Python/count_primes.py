class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        prime_count = 1 # make up for excluding 2 as a prime number
        composites = [False] * n # assume all numbers to be prime
        
        for i in range(3, n, 2): # we only use odd numbers for primes (except 2)
            if not composites[i]:
                prime_count += 1
                j = i ** 2 # multiplying odds by odds, to get odds
                while j < n:
                    composites[j] = True # get rid of numbers having a prime coefficient
                    j += 2 * i # skip over an even result
        return prime_count
