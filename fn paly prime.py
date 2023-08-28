def paly(n):
    paly=0
    while n!=0:
        rem=n%10
        paly=paly*10+rem
        n//=10
    return paly
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
n=14
if n==paly(n) and prime(n):
    print('pp')
else:
    print('not pp')
