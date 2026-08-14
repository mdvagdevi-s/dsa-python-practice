a=[3,4,6,1,2]

target=6

for i in range(len(a)):
    if a[i]==target:
        print("Found at index",i)
        break


    #why we use break statement here? 
    # that is beacuse once target is found
    #  no need of continuing the loop just stop the loop here .