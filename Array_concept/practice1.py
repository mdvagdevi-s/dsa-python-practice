a = [5, 2, 8, 1, 9]
largest=a[0]

for i in range(1,len(a)):
    if a[i]>largest:
            largest=a[i]

print("Largest element:",largest)