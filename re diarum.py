
';def arm(n,a):
    if n==0:
        return 0
    return (n%10)**a+arm(n//10,a-1)
n=135
a=len(str(n))
if n==arm(n,a):
    print('disarm')
else:
    print('not')
