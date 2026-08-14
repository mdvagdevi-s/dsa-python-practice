a = [34, 12, 56, 7, 89, 23]
small=a[0]
for i in range(len(a)):
    if a[i]<small:
        small=a[i]

print("Smallest element is:",small)