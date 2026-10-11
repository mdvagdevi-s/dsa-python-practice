num=5432
count=0
while num>0:
    digit=num%10
    count+=1
    num=num//10
print("The number of digits in the given number is:",count)