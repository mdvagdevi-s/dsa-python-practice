a = [2, 4, 1, 5, 3]
prefix = []
for i in range(len(a)):
    if i == 0:
        prefix.append(a[i])
    else:
        prefix.append(prefix[i - 1] + a[i])

l=1
r=3
if l==0:
    res=prefix[l]

else:
    res=prefix[r]-prefix[l-1]

print("Range sum:",res)