class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if x<0:
            return False
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if num==rev:
            return True
        else:
            return False
obj=Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))
print(obj.isPalindrome(1221))
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if x<0:
            return False
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if num==rev:
            return True
        else:
            return False
obj=Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))
print(obj.isPalindrome(0))