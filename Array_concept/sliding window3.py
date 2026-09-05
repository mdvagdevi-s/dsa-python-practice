a = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
max_length = 0

for right in range(len(a)):

    current_sum += a[right]

    while current_sum > target:
        current_sum -= a[left]
        left += 1

    length = right - left + 1
    max_length = max(max_length, length)

print(max_length)