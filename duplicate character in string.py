s='shashi'
a=''
for i in s:
    if i not in a:
        a+=i
print(a)
#----------------------------------------
s='shasdddhi'
a=[] 
for i in s:
    if s.count(i)>1 and i not in a:
        print(i)
        a.append(i)
