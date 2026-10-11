n=121
num=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==num:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")