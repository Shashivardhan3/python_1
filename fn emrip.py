def emrip(n):
    ep=0
    while n!=0:
        rem=n%10
        ep=ep*10+rem
        n//=10
    return ep
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
n=17
if n!=emrip(n) and prime(n) and prime(emrip(n)):
    print('ep')
else:
    print('not ep')
