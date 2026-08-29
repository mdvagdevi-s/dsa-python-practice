a=[1,2,3,4]

res=[1]*len(a)

prefix=1

for i in range(len(a)):
    res[i]=prefix
    prefix*=a[i]

suffix=1
for i in range(len(a)-1,-1,-1):
    res[i]*=suffix
    suffix*=a[i]

print(res)