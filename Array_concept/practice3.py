a = [12, 7, 25, 9, 30]
target = 25
found=False
for i in range(len(a)):
    if a[i]==target:
        found=True
        break

if found:
    print("Target found at index:",i)
else:
    print("Target not found")
