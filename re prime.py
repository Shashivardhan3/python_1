7def prime(n,i):
    if n<=1 or n%i==0:
        return False
    if i>n//2+1:
        return True
    return prime(n,i+1)
n=5
i=2
if prime(n,i):
    print('prime')
else:
    print('not prime')
#-----------------------------------------------------------------------------------------------------------------------
def prime(n,i):
    if i==n+1:
        return 0
    return (1 if n%i==0 else 0)+prime(n,i+1)
n=5
i=2
if prime(n,i)==2:
    
    print('prime')
else:
    print('not prime')
