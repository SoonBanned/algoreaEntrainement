K = int(input())
nbNombres = int(input())
L = []
somme = []


for iNombre in range(nbNombres):
    L.append(int(input()))
    

c =0
for j in range(K-1):
    c+= L[j]
    
for i in range(nbNombres-K+1):
    
    c += L[K+i-1]
    somme.append(c)
    c -= L[i]
    
    

print(max(set(somme)))