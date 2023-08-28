def sunny(n,i):
    if i**2>n+1:
        return False
    if i**2==n+1:
        return True
    return sunny(n,i+1)
n=6
if sunny(n,1):
    print('sunny')
else:
    print('not')
