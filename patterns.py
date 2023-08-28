#patterns
n=5
for i in range(1,n+1):
    print('* ' * i)

print('\n')

n=5
for i in range(1,n+1):
    
    print('* ' * n)

print('\n')

n=5
for i in range(5,0,-1):
    print('* ' * i)

print('\n')

n=5
while(n!=0):
    print('* '* n)
    n-=1

print('\n')


n=1
while(n<=5):
    print('* ' * n)
    n+=1
print('\n')

n=5
for i in range(1,n+1):
    print('  '*(n-i),'* '*(i))

print('\n')
n=5
for i in range(5,0,-1):
    print('  '*(n-i),'* '*(i))

print('\n')

n=5
i=1
while(i!=n+1):
    print('  '*(n-i),'* '*(i))
    i+=1
print('\n')
n=5
i=n
while(i!=0):
    print('{}{}'.format('  '*(n-i),('* ' * i)))
    
    i-=1
print('\n')


n=5
for i in range(1,n+1):
    print('{}{}{}'.format('  '*(n-i),'* '*i,'* '*(i-1)))

print('\n')


n=5
for i in range(n,0,-1):
    print('{}{}{}'.format('  '*(n-i),'* '*i,'* '*(i-1)))

print('\n')

n=5
star=1
space=n
while(space!=0):
    print('{}{}'.format('  '*(space-1),'* ' *star))
    star+=2
    space-=1

print('\n')

n=5
star=9
space=0
while(space!=n):
    print('{}{}'.format('  '*space,'* ' *star))
    star-=2
    space+=1







