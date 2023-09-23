height = 5

for i in range(height):
    for j in range(height):

        if i ==height-1 or j == 0:
            print("*", end=" ")
        else :
            print(" ",end=" ")
    print()