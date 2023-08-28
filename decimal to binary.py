n=21
bi=0
a=1
while n!=0:
    rem=n%2
    bi=bi+rem*a
    n//=2
    a*=10
print(bi)
