def auto(n,i):
    if n==0:
        return 1
    return (n%10 == i%10) and auto(n//10 ,i//10)
n=23
i=n**2
if auto(n,i):
    print('auto')
else:
    print('not auot')
