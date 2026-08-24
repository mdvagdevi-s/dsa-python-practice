arr = [1, 2, 3]

for start in range(len(arr)):
    for end in range(start, len(arr)):
        # print the current subarray
        print(arr[start:end+1])