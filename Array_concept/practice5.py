a = [10, 20, 15, 40, 50]
is_sorted=True

for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")