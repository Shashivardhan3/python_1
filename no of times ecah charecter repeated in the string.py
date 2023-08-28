s='shashi'
a=[]
for i in s:
    if i not in a:
        print('{} ={}'.format(i,s.count(i)))
        a.append(i)
#----------------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
a=''
for i in s:
    if i not in a:
        print("{}={}".format(i,s.count(i)))
        a+=i
#----------------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
print(d)
#----------------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
