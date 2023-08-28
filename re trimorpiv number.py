def tri(n,i):
    if n==0:
        return 1
    return (n%10 == i%10) and tri(n//10 ,i//10)
n=249
i=n**3
if tri(n,i):
    print('tri')
else:
    print('not')
        
