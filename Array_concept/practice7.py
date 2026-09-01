a = [0, 1, 0, 3, 12]
x=0
for i in range(len(a)):
    if a[i]!=0:
        a[x],a[i]=a[i],a[x]
        x+=1
    else:
        pass

print(a)