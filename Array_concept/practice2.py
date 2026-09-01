a = [10, 20, 5, 20, 30, 20]
count=0
target=20
for i in range(len(a)):
    if a[i]==target:
        count+=1

print("20 occurs",count,"times")