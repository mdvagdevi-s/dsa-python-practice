s="education"
vowels="aeiou"
count=0

for char in s:
    if char.isalpha() and char not in vowels:
        count+=1
print("total consonents:",count)