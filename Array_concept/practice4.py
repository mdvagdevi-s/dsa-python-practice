a = [10, 25, 7, 40, 15]
lar=a[0]
sec=a[0]
for i in range(1,len(a)):
    if a[i]>lar:
        sec=lar
        lar=a[i]
    elif a[i]>sec:
        sec=a[i]
print("Secod largest element:",sec)