n=123
a=len(str(n))
b=0
c=n
while n!=0:
    rem=n%10
    b+=rem**a
    n//=10
if c==b:
    print('armstrong')
else:
    print('not armstrong')
    
print('\n')
n=153
a=str(n)
b=len(a)
add=0
for i in a:
    add+=int(i)**b
if add==n:
    print('armstrong')
else:
    print('not armstrong')
