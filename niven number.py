n=1256
add=0
copy=n
while n!=0:
    rem=n%10
    add+=rem
    n//=10
if copy%add==0:
    print('niven')
else:
    print('not niven')
