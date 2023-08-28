n=17
c=0
while n!=0:
    if n%2==1:
        c+=1

    n//=2
if c%2==0:
    print('evil')
else:
    print('odus')
