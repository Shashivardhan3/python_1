def niven(n):
    
    add=0
    while n!=0:
        rem=n%10
        add+=rem
        n//=10
    return add

n=123
if n%niven(n)==0:
    print('niven')
else:
    print('not niven')
