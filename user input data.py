n=int(input('enter the no of values:'))
a=input('enter the values:')
l=[]

for i in range(n):
        l.append(int(a))
print(l)
print('\n')
#---------------------------------------------------------------------------------------------------
n=int(input('enter the no of values:'))
l=[]

for i in range(n):
        l.append(int(input('enter the values:')))
print(l)
print('\n')
#---------------------------------------------------------------------------------------------------
n=int(input('enter the no of values:'))
l=list(map(int,input('enter the values:').split()))
print(l)
print('\n')
#---------------------------------------------------------------------------------------------------
n=int(input('enter the no of values:'))
l=list(map(lambda a:int(input('enter the values:')),range(n)))
print(l)
