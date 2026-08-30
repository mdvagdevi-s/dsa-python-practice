a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left=0
right=len(a)-1
max_water=0
while left<right:
    height=min(a[left],a[right])
    width=right-left
    water=height*width
    max_water=max(max_water,water)
    if a[left]<a[right]:
        left+=1
    else:
        right-=1
print("Maximun water:",max_water)