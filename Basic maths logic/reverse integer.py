class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        sign=1
        if x<0:
            sign=-1
            x=x*-1
        while x>0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        if not -2**31<=reverse*sign<=2**31-1:
            return 0
        return reverse*sign
solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(1534236469))
print(solution.reverse(120))