n=49
while n>9:
    add=0
    while n!=0:
        rem=n%10
        add+=rem**2
        n//=10
    n = add
if  add==1:
    print('happy')
else:
    print('not')
