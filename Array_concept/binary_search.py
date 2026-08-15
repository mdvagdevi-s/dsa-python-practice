a= [2, 5, 8, 12, 16, 20, 25]
target = 16
low=0
high=len(a)-1

while low<=high:
    mid=(low+high)//2
    if a[mid]==target:
        print("Found at index",mid)
        break
    elif a[mid]<target:
        low=mid+1

    else:
        high=mid-1