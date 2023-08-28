def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
for i in range(40,81):
    if prime(i):
        print(i)
print('\n')
#----------------------------------------------------------------------------------------------------
        
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
for i in range(70,19,-1):
    if prime(i):
        print(i)
print('\n')
#----------------------------------------------------------------------------------------------------
        
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
i=1
c=0
while c!=5:
    if prime(i):
        print(i)
        c+=1
    i+=1
    
print('\n')
#----------------------------------------------------------------------------------------------------
        
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
print(prime(6))
print('\n')
print('\n')
#----------------------------------------------------------------------------------------------------
        
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
c=0
for i in range(20,40):
    if prime(i):
        if c==5:
            print(i)
            break
    
