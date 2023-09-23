# to remove the duplicate in the list

list = [3,4,6,2,5,3,8]
dup = []
for x in list:
    if x not in dup:
        dup.append(x)
print(dup)
    
    
        
