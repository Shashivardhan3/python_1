def fact(n):
    if n==0 or n==1:
        return 1
    return n%10*fact(n-1)
print(fact(5))
