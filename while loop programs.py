#Write a while loop that prints numbers from 1 to 10.
a=1
while(a<=10):
    print(a)
    a+=1
print('\n')
#------------------------------------------------------------------------------
#Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.
#Expected Input: 5
#Expected Output: 15 (1 + 2 + 3 + 4 + 5)

n=int(input('enter the number:'))
add=0
a=1
while a<=n:
    add+=a
    a+=1
print(add)
print('\n')
#------------------------------------------------------------------------------
#Write a while loop that prints even numbers from 2 to 10.
a=2
while(a<=10):
    print(a)
    a+=2
print('\n')
#------------------------------------------------------------------------------
##Create a while loop that keeps prompting the user for a number until they enter a negative number.
##Expected Input: 5, 10, -2
##Expected Output: (No output, just prompt for input)
while True:
    n= int(input("Enter a number: "))
    if n < 0:
        break
print('\n')
#------------------------------------------------------------------------------
  
#Write a while loop that counts down from 10 to 1.
a=10
while(a>=1):
    print(a)
    a-=1

print('\n')
#------------------------------------------------------------------------------

##Create a while loop that asks the user to guess a secret number (e.g., 7) and continues until the correct number is guessed.
##Expected Output: (Depends on user input)


secret=7

while True:
    guess =int(input("guess the secret number: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again! Incorrect guess.")

print('\n')
#------------------------------------------------------------------------------

##Write a while loop that calculates the factorial of a given number.
##Expected Input: 4
##Expected Output: 24 (4! = 4 * 3 * 2 * 1 = 24)

n=int(input('enter the number:'))
mul=1
while n>1:
    mul*=n
    n-=1
print(mul)

print('\n')
#------------------------------------------------------------------------------

#Create a while loop that prints the square of numbers from 1 to 5. 

n=1
while n<=5:
    print(n**2)
    n+=1
print('\n')
#------------------------------------------------------------------------------
##Write a while loop that reads numbers from the user until they enter the number 0. Then, it prints the sum of all the entered numbers.
##Expected Input: 3, 5, 2, 0
##Expected Output: 10 (3 + 5 + 2)

n=int(input("Enter a number: "))
add=0
while n!=0:
    add+=n
    n=int(input("Enter a number: "))
print(add)
print('\n')
###------------------------------------------------------------------------------
##Create a while loop that prints the Fibonacci series up to n.
##Expected Input: 10
n=int(input('enter a number'))
a,b=0,1
while a<=n:
    print(a)
    a=b
    b=a+b







































































