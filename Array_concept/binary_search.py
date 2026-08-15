a= [2, 5, 8, 12, 16, 20, 25]
target = 100
low=0
high=len(a)-1
found=False

while low<=high:
    mid=(low+high)//2
    if a[mid]==target:
        print("Found at index",mid)
        found=True
        break
    elif a[mid]<target:
        low=mid+1

    else:
        high=mid-1
if not found:
    print("Not found!")