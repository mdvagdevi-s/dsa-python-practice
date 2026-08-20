a=[2,7,11,15]
target=9

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            print("Target is found in the index:",i,j)