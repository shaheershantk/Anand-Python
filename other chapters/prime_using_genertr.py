def genPrimes(n):
    e=0
    for j in range(2,1000):
        if j==2:
            yield j
        if e==n:
            break
        for i in range(2,j):
            if (j%i) ==0:
                j+=1
                pass
            elif (j%i)!=0 and i==j-1:
                yield j
                e+=1

    