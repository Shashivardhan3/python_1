def niven(n):
    if n==0:
        return 0
    return n%10+niven(n//10)
n=123
if n%niven(n)==0:
    print('niven')
else:
    print('not')
