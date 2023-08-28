def rev(n,a):
    if n==0:
        return 0
    return (n%10)*a+rev(n//10,a//10)
n=1234
a=len(str(n))
print(rev(n,(10**(a-1))))
