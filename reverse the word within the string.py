s='WE WANT SUNDAY CLASS'
l=s.split()
a=[]
for i in l:
    b=i[::-1]+''
    a.append(b)
print(' '.join(a))
#---------------------------------------------------------------------------------------------------------------
print('\n')
s='WE WANT SUNDAY CLASS'
l=s.split()
a=''
for i in l:
    b=i[::-1]+' '
    a+=b
print(a.strip())
#---------------------------------------------------------------------------------------------------------------
print('\n')
s='WE WANT SUNDAY CLASS'
ss=''
res=''
for i in s:
    if i!=' ':
        ss+=i
    else:
        res+=ss[::-1]+' '
        ss=''
res+=ss[::-1]
print(res)

