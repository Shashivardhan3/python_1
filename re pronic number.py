def pronic(n,i):
    if i*(i+1)>n:
        return False
    if i*(i+1)==n:
        return True
    return pronic(n,i)
n=12
if pronic(n,1):
    print('pronic')
else:
    print('not')
