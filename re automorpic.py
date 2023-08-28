def automorpic(n,s):
    if n==0:
        return 1
    r1=n%10
    r2=s%10
    if r1 != r2:
        return 0
    return automorpic(n//10,s//10)
n=25
i=n**2
if automorpic(n,i):
    print('automorpic')
else:
    print('not')
