class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        sieve = [True] * n
        sieve[0] = sieve[1] = False

        i = 2
        while i * i < n:          # only sieve up to sqrt(n)
            if sieve[i]:
                j = i * i         # start marking at i*i
                while j < n:
                    sieve[j] = False
                    j += i
            i += 1

        # count remaining True values with a while loop
        count = 0
        k = 2
        while k < n:
            if sieve[k]:
                count += 1
            k += 1
        return count
sol=Solution()
print(sol.countPrimes(30))