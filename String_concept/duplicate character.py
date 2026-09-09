s = "programming"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in freq:
    if freq[ch]>1:
        print("Duplicate characters are:",ch)