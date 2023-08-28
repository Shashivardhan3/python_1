def d2b(n,a):
    if n==0:
        return 0
    return (n%2)*a+d2b(n//2,a*10) 
n=13
a=1
print(d2b(n,a))
