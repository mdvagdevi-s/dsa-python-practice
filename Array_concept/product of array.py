a = [1, 2, 3, 4]
res = []

for i in range(len(a)):
    product = 1

    for j in range(len(a)):
        if i != j:
            product *= a[j]

    res.append(product)

print(res)