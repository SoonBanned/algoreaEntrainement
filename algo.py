import numpy
"""
import time
t1 = time.clock()
"""
K = int(input())
nbNombres = int(input())
L = []
somme = []


for iNombre in range(nbNombres):
    L.append(int(input()))


B = numpy.asarray(L)

for i in range(nbNombres-K+1):
    somme.append(B[i:i+K].sum())


print(max(set(somme)))