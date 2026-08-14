arr = [12, 45, 7, 89, 23, 56]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("Largest element:",max)