def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def strong(n):
    if n==0:
        return 0
    return fact(n%10)+strong(n//10)
n=145
if strong(n)==n:
    print('str')
else:
    print('not')
    

