def disarum(n,p):
    add=0
    while n!=0:
        rem=n%10
        add+=rem**p
        n//=10
        p-=1
    return add
n=165
p=len(str(n))
if n==disarum(n,p):
    print('disarum')
else:
    print('not disarum')
