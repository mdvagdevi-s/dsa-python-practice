s="python" 
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

#or

a="python"
reverse=""
for i in range(len(a)-1,-1,-1):
    reverse+=a[i]
print(reverse)