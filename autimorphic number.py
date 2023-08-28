n=25
sq=n**2

while n!=0:
    r1=n%10
    r2=sq%10
    if r1!=r2:
        print('not auto')
        break
    n//=10
    sq//=10
else:
    print('auto ')

print('\n')
#--------------------------------------------------------------------------------------
n=23
a=len(str(n))
sq=n**2
rem=sq%(10**a)
if n==rem:
    print('auto')
else:
    print('not auto')
