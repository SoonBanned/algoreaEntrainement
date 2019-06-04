nb = int(input())
#Liste contenant en 0 les nombres croisés et en 1 leur indice
TEMP = [[],[]]
#Liste contenant toute les distances
Dist = []

for i in range(nb):
    x = int(input())
    
    #On teste si x est déjà croisé, si il l'est on retrouve son index, le supprime et réutilise cet index pour calculer la distance
    if x in set(TEMP[0]):
        j = TEMP[0].index(x)
        TEMP[0].pop(j)
        Dist.append(i-TEMP[1].pop(j))
    #on ajoute respectivement le nombre et son index dans L[0] et L[1]
    TEMP[0].append(x)
    TEMP[1].append(i)
        


print(min(set(Dist)))
