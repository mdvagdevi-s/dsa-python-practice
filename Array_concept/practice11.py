a = [2, 4, 1, 5, 3]
prefix=[]
for i in range(len(a)):
    if i==0:
        prefix.append(a[i])
    else:
        prefix.append(prefix[i-1]+a[i])

print(prefix)