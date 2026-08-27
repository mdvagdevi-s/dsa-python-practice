a = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n=len(a)
expected_sum=n*(n+1)//2
actucal_sum=0
for x in a:
    
    actucal_sum+=x

missing_num=expected_sum-actucal_sum

print("Missing number:",missing_num)
