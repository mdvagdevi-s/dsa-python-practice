a= [10, 25, 7, 40, 15]
largest=a[0]
second=a[0]


for i in range(1,len(a)):
    if a[i]>largest:
        second=largest
        largest=a[i]

    elif a[i]>second:
        second=a[i]

print("Second Largest element is:",second)