def strong(n):
    add=0
    while n!=0:
        rem=n%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        add+=fact
        n//=10
    return add
n=145
if n==strong(n):
    print('strong ')
else:
    print('not strong')


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def strong(n,c):
    add=0
    while n!=0:
        rem=n%10
        add+=fact(rem)
        n//=10
    return add==c
n=145
if strong(n,c):
    print('strong')
else:
    print('not strong')
