def add(n):
    add=0
    while n!=0:
        rem=n%10
        add+=rem
        n//=10
    return add
print(add(123))
