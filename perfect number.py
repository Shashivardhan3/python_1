n=28
add=0
for i in range(1,n//2+1):
    if n%i==0:
        add+=i
if add==n:
    print('perfect')
else:
    print('not perfect')
