s='DONT FIRE THE FIRE'
l=s.split()
a=0
for i in l:
    if l.count(i)>a:
        a=l.count(i)
b=''
for i in l:
    if l.count(i)==a and i not in b:
        print(i)
        b+=i
#---------------------------------------------------------------------------------------------------------------------
print('\n')
s='DONT FIRE THE FIRE'
l=s.split()
a=[]
for i in l:
    if l.count(i)>1 and i not in a:
        print(i)
        a.append(i)
#---------------------------------------------------------------------------------------------------------------------
print('\n')
s='DONT FIRE THE FIRE'
l=s.split()
a=[]
for i in l:
    if l.count(i)>1 and i not in a:
        print(i)
        a.append(i)
b=0
for i in l:
    if l.count(i)>b:
        b=l.count(i)
        
