a = [3, 5, 2, 7]
prefix=[]

for i in range(len(a)):
    if i==0:
        prefix.append(a[i])
    else:
        prefix.append(prefix[i-1]+a[i])
print(prefix)