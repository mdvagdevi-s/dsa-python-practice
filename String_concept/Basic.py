s="hello"
print(s[0])
print(s[4])
print(len(s))

for i in range(len(s)):  #or for char in s:
    print(s[i])  # Print each character in the string

s="H"+s[1:]
print(s)

word="python"
for i in range(len(word)):
    print(i,word[i])