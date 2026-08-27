a=[3, 3, 4, 2, 3, 3, 5]
freq={}

for value in a:
    if value in freq:
        freq[value]+=1
    else:
        freq[value]=1

for value in freq:
    if freq[value]>len(a)//2:
        print("Majority element:",value)