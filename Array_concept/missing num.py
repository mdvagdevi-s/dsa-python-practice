a=[3,0,1]
n=len(a)
expected_sum=n*(n+1)//2
actucal_sum=0
for x in a:
    
    actucal_sum+=x

missing_num=expected_sum-actucal_sum

print("Missing number:",missing_num)
