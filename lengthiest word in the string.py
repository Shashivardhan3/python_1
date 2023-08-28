s='we are in the class'
l=s.split()
a=0
for i in l:
    if len(i)>a:
        a=len(i)
b=''
for i in l:
    if len(i)==a and i not in b:
        print(i)
        b+=i
#---------------------------------------------------------------------------------------------------------------------
print('\n')
s='we are in the class'
l=s.split()
a=''
for i in l:
    if len(i)>1 and i not in a:
        print(i)
        a+=i
b=0
for i in l:
    if len(i)==a:
        print(i)
        b+=i
