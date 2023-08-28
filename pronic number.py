n=12
a=1
for i in range(1,n):
    if i*(i+1)==n:
        print('pronic')
        break
    a+=1
else:
    print('not pronic')
print('\n')
#--------------------------------------------------------------------------------------------
n=15
i=1
while i**2<=n:
    if i*(i+1)==n:
        print('p2ronic')
        

        break
    i+=1
else:
    print('not')
    
