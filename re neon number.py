def neon(n):
    if n==0:
        return 0
    return n%10+neon(n//10)
n=12
if n==neon(n**2):
    print('neon')
else:
    print('not')
