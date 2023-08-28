def perfect(n,i,a):
    if i>=n:
        return n==a
    if n%i==0:
        a+=i
    return perfect(n,i+1,a)
n=28
if perfect(n,1,0):
    print('perfect')
else:
    print('not')
