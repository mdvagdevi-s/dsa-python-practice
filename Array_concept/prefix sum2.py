a = [3, 5, 2, 7, 4, 6]
prefix=[]

for i in range(len(a)):
    if i==0:
        prefix.append(a[i])
    else:
        prefix.append(prefix[i-1]+a[i])
l=2
r=5
if l==0:
    result=prefix[r]
else:
    result=prefix[r]-prefix[l-1]

print("Range sum:",result)