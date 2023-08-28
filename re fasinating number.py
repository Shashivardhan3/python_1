def fasi(n,i):
    if str(i) not in n:
        return i
    return fasi(n,i+1)
n=12
i=1
a=str(n*1)+str(n*2)+str(n*3)
if fasi(a,i):
    print('f')
else:
    print('nf')

def fasi(n,i):
    if a!=0:
        if str(i) not in n:
            return i
        return fasi(n,i+1)
    return i
n=324
i=1
b=str(n*1)+str(n*2)+str(n*3)
if fasi( b,i)==10:
    print('fasi')
else:
    print('not ')
