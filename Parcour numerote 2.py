import time
t1 = time.clock()
n = int(input())
v = [int(input()) for _ in range(n)]

t = 0

for i in range (n):
    a = v[i]
    c = 1
    
    while a-1 != i:
        
        a = v[a-1]
        c +=1
        
        if c == n or (t1 - time.clock()) > 0.20:
            break
        
    
    if c > t:
        t = c
    
    if c == n or (t1 - time.clock()) > 0.20:
        break


print(t)