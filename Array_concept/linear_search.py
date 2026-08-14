a = [5, 12, 8, 20, 15]
target = 20

for i in range(len(a)):
    if a[i]==target:
        print("Found at index",i)
        break


    #why we use break statement here? 
    # that is beacuse once target is found
    #  no need of continuing the loop just stop the loop here .