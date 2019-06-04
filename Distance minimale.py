nb = int(input())
TEMP = [[],[]]
Dist = []

for i in range(nb):
    x = int(input())
    
    if x in set(TEMP[0]):
        j = TEMP[0].index(x)
        TEMP[0].pop(j)
        Dist.append(i-TEMP[1].pop(j))
    TEMP[0].append(x)
    TEMP[1].append(i)
        

        
print(min(set(Dist)))