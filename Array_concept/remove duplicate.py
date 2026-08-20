a=[1,1,2,2,3,4,4]
i=0
for j in range(i+1,len(a)):
    if a[i]!=a[j]:
        i+=1
        a[i]=a[j]

print(a[:i+1])
