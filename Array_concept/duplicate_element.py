arr = [4, 2, 7, 2, 9, 4, 5]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print("Duplicate:",arr[i])


