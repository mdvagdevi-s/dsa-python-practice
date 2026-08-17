a=[10,20,30,40,50]
k=6
k=k%len(a)
def reverse(a,l,r):
    while l<r:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
reverse(a,0,k-1)

reverse(a,k,len(a)-1)

reverse(a,0,len(a)-1)

print(a)

