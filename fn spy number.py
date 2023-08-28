def add(n):
    add=0
    while n!=0:
        rem=n%10
        add+=rem
        n//=10
    return add
def mul(n):
    mul=1
    while n!=0:
        rem=n%10
        mul*=rem
        n//=10
    return mul
n=123
if add(n)==mul(n):
    print('spy number')
else:
    print('not spy')
#----------------------------------------------------------------------------------------------------------
def spy(n):
    add=0
    mul=1
    while n!=0:
        rem=n%10
        add+=rem
        mul*=rem
        n//=10
    if add==mul:
        return True
    return False
print(spy(123))
#----------------------------------------------------------------------------------------------------------
def spy(n):
    add=0
    mul=1
    while n!=0:
        rem=n%10
        add+=rem
        mul*=rem
        n//=10
    return add==mul
print(spy(123))
#----------------------------------------------------------------------------------------------------------
def spy(n):
    add=0
    mul=1
    while n!=0:
        rem=n%10
        add+=rem
        mul*=rem
        n//=10
    return add==mul
n=123
if spy(n):
    print('spy')
else:
    print('not s')

