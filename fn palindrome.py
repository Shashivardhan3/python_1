def pali(n):
    pali=0
    while n!=0:
        rem=n%10
        pali=pali*10+rem
        n//=10
    return pali
n=123
if n==pali(n):
    print('pali')
else:
    print('not pali')
