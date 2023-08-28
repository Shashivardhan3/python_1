for i in range(1,6):
    for j in range(5):
        print('*',end='')
    print()
#=====================================================================
print('\n')
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()
#=====================================================================
print('\n')
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end="")
    print()
#=====================================================================
print('\n')
##Create a nested loop to find and print prime numbers from 2 to 20.
##Expected Input: None
##Expected Output: 2 3 5 7 11 13 17 19
for i in range(2, 21):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
#=====================================================================
print('\n')
##Create a nested loop to find and print the factorial of numbers from 1 to 5.
##Expected Input: None
##Expected Output: 1 2 6 24 120
for i in range(1,6):
    
    fact=1
    for j  in range(1,i+1):
        fact*=j
    print(fact,end=' ')
#=====================================================================
print('\n')
##Write a nested loop to calculate and print the sum of numbers from 1 to 5 using nested iteration.
##Expected Input: None
##Expected Output: 15
for i in range(1,6):
    add=0
    for j in range(1,i+1):
        add+=j
print(add)
#=====================================================================
print('\n')
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=' ')
    print()
#=====================================================================
print('\n')

for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(i * j, end=" ")
    print()
#=====================================================================
print('\n')
for i in range(3):
    print(" "*(2 - i)+"*"*(2*i+1))
for i in range(1, 3):
    print(" " * i + "*" * (5 - 2 * i))
print()
#=====================================================================
print('\n')
for i in range(5):
    if i==0 or i==4:
        print('*'*5)
    else:
        print('*'*1+' '*3+'*'*1)
print()
    















































