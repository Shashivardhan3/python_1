n=int(input('enter the number:'))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
if a==2:
    print('prime')
else:
  print('not prime')
print('\n')
n=int(input('enter the number:'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print('not prime')
            break

    else:
        print('prime')
else:
    print('not prime')
             
            
    
'''
        
n = int(input('Enter the number: '))
if n > 1:
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')
else:
    print('Not prime')
'''
