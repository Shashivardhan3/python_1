n=15
em=0
copy=n
while n!=0:
    rem=n%10
    em*=10+rem
    n//=10
if copy!=n:
    for i in range(2,copy//2+1):
        if copy%i==0:
            print('not emrip')
            break
    else:
        for i in range(2,ep//2+1):
            if em%i==0:
                print('not emrip')
                break
        else:
            print('emrip')
else:
    print('emrip')
        
