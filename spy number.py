n=145
add=0
mul=1
while n!=0:
    rem=n%10
    add+=rem
    mul*=add
    n//=10
if add==mul:
    print('spy')
else:
    print('not spy')
