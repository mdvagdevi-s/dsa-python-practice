n=1634
num=n
total=0
nod=len(str(n))
while n>0:
    i=n%10
    total+=i**nod
    n=n//10
if total==num:
    print("The given number is Armstrong ")
else:
    print("The given number is not Armstrong ")