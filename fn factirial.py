def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return True
n=5
print(fact(n))
print('\n')
#========================================================================================================================



def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
print(fact(5))#fact function does not have a return statement. so output is None
print('\n')
#========================================================================================================================



def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
print(fact(5))
