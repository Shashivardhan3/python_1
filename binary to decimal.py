n=10101
de=0
a=1

while n!=0:
    rem=n%10
    de+=rem*a
    n//=10
    a*=2
print(de)
