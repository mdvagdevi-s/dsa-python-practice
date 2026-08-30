a = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = 5

while mid<=high:
    if a[mid]==0:
        a[low],a[mid]=a[mid],a[low]
        low+=1
        mid+=1

    elif a[mid]==1:
        mid+=1

    else:
        a[mid],a[high]=a[high],a[mid]
        high-=1
print(a)