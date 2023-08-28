n=135
a=len(str(n))
b=0
c=n
while n!=0:
    rem=n%10
    b+=(rem**a)
    n//=10
    a-=1
if b==c:
    print('disarum')
else:
    print('not disarum')

print('\n')

n=89
a=str(n)
b=1
c=0
for i in a:
    c+=int(i)**b
    b+=1
if c==n:
    print('disarum')
else:
    print('not')
