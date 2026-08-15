arr = [2, 2, 2, 5, 5]
duplicates=set()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            duplicates.add(arr[i])
print(duplicates)
