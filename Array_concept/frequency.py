arr = [2, 3, 2, 5, 3, 2, 7]
freq={}

for value in arr:
    if value in freq:
        freq[value]+=1
    else:
        freq[value]=1

print(freq)