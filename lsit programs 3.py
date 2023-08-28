s=[21,45,21,10,56,10,10,21]
a=[]
for i in s:
   if s.count(i)==1:
       a.append(i)
print(a)
print('\n')
#[45, 56]

#-----------------------------------------------------------------------------
s=[21,45,21,10,56,10,10,21]
a=[]
for i in s:
    if s.count(i)>1 and i not in a:
        a.append(i)
print(a)
#-----------------------------------------------------------------------------
s=[21,45,21,10,56,10,10,21,21]
a=[]
h=0
for i in s:
    if s.count(i)>h:
        h=s.count(i)
for i in s:
    if s.count(i)==h and i not in a:

        a.append(i)
print(a)

