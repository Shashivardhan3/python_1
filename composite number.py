n=6
a=0

for i in range(1,n+1):
    if n%i==0:
        a+=1
       
if a>2:
    print('cpn')
else:
    print('not')

print('\n')


n=7
for i in range(2,n//2+1):
    if n%i==0:
        print('cop')
        break
else:
    print('not')
    
    
