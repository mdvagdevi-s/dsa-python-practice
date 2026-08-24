arr = [1, 2, 3]
for start in range(len(arr)):
    current_sum = 0

    for end in range(start, len(arr)):
        current_sum += arr[end]
        print(current_sum)