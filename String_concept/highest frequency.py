s="banana"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
max_freq=0
for ch in freq:
    if freq[ch]>max_freq:
        max_freq=freq[ch]
        max_char=ch

print("Highest frequency character is:",max_char)