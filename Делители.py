a = 125873
b = 136762
def del_fast(n):
    d = []
    q = round(n**(1/2))
    if q*q == n: d.append(q)
    for k in range(1,q):
        if n % k == 0:
            d.append(k)
            d.append(n//k)
    d.sort()
    return d
for i in range(a,b+1):
    if len(del_fast(i)) == 5: print(i,':',del_fast(i))
            
    
            