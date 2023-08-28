def b2d(n,a):
    if n==0:
        return 0
    return (n%10)*a+b2d(n//10,a*2)
n=10101
a=1
print(b2d(n,a))
