a=[2,7,11,15]
t=9
seen={}
for i in range(len(a)):
    c=a[i]
    n=t-c
    if n in seen:
        print("Found:",seen[n],i)

    else:
        seen[c]=i