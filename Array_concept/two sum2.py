a=[2,7,11,15]
target=18
seen={}

for i in range(len(a)):
    current=a[i]
    needed=target-current

    if needed in seen:
        print("Found in the index:",seen[needed],i)

    else:
        seen[current]=i