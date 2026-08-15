arr = [5, 2, 5, 7, 5, 9]
target = 5
count=0

for i in range(len(arr)):
    if arr[i]==target:
        count+=1
print("5 occurs",count,"times")

