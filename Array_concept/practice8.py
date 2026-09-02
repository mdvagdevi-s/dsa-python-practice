a = [4, 2, 7, 2, 9, 4, 5]

seen = set()
duplicates = set()

for value in a:

    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)

print("Duplicates:", duplicates)