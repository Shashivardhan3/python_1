n=1212
pd=0
copy=n
while n!=0:
    rem=n%10
    pd = pd * 10 + rem
    n//=10
if copy==pd:
    print('palindrome')
else:
    print('not palindrome')
