arr = [1, 2, 3]
k = 3
seen = {0: 1}
prefix_sum = 0
count = 0

for i in range(len(arr)):
    prefix_sum += arr[i]

    needed = prefix_sum - k

    if needed in seen:
        count += seen[needed]

    if prefix_sum in seen:
        seen[prefix_sum] += 1
    else:
        seen[prefix_sum] = 1
print(count)