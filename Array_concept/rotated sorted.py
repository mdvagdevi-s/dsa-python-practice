a=[4,5,6,7,0,1,2]
target=1

low=0
high=6
mid=3

while low<=high:
    mid=(low+high)//2
    if a[mid]==target:
        print("Found at index:",mid)
        break

    if a[low]<=a[mid]:
        # left half is sorted
        if a[low]<=target<a[mid]:
            high=mid-1
        else:
            low=mid+1

    else:
        # right half is sorted
        if a[mid]<=target<=a[high]:
            low=mid+1
        else:
            high=mid-1
