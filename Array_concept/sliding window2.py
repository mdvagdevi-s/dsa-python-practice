a=[2,3,1,2,4,3]
target=7

left=0
current_sum=0
min_length=float("inf")

for right in range(len(a)):
    current_sum+=a[right]

    while current_sum>=target:
        length=right-left+1
        min_length=min(min_length,length)
        current_sum-=a[left]
        left+=1

print(min_length)