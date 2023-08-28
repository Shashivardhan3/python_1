n=145
add=0
copy=n
while n!=0:
    rem=n%10
    a=1
    for i in range(1,rem+1):
        a*=i
    add+=a
    n//=10
if copy==add:
    print('strong number')
else:
    print('not strong number')


n = 145
add = 0
copy = n

while n != 0:
    rem = n % 10
    fact = 1
    for i in range(1, rem+1):
        fact *= i
    add += fact
    n //= 10

if copy == add:
    print('strong number')
else:
    print('not strong number')


