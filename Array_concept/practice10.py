a = [1, -2, 3, -4, -5, 6]
l=0
r=len(a)-1
while l<r:
    if a[l]<0:
        l+=1
    elif a[r]>=0:
        r-=1
    else:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
print(a)
