n=131
pp=0
copy=n
while n!=0:
    rem=n%10
    pp=(pp*10)+rem
    n//=10
if pp!=copy:
    print('not not paly prime')
else:
    
    if copy > 1:
        
        for i in range(2,copy//2+1):
            
            if copy%i==0:
                
                print('not paly prime')
        else:
            
            print('paly prime')
    else:
        print(' not palyprime')
print('\n')

#-------------------------------------------------------------------------------------------------------------------------------------
            
n = 11
pp = 0
copy = n

while n != 0:
    rem = n % 10
    pp=(pp*10)+rem
    n //= 10

if pp != copy:
    print('not palindrome')
if copy > 1:
    for i in range(2, copy // 2 + 1):
        if copy % i == 0:
            print('not prime')  # Corrected from 'not papp'
else:
    print('palindrome')
print('\n')
#-------------------------------------------------------------------------------------------------------------------------------------
n=131
copy=n
pp=0
while n!=0:
    rem=n%10
    pp=(pp*10)+rem
    n//=10
if copy==pp and copy>1:
    for i in range(2,copy//2+1):
        if copy%i==0:
            print("not paly prime")
            break
    else:
        print('paly prime')
else:
    print('not palyprime')






























            
