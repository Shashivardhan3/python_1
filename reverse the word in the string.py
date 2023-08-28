s='SHASHI VARDHAN'
l=s.split()
a=l[::-1]
print(a)
print(''.join(a))
print(' '.join(a))
#---------------------------------------------------------------------------------------------------------------
print('\n')
s='WE WANT SUNDAY CLASS'
res=''
ss=''
for i in s:
    if i!=' ':
        ss+=i
    else:
        res=ss+' '+res
        ss=''
res=ss+' '+res
print(res.strip())

#---------------------------------------------------------------------------------------------------------------
print('\n')
s='WE WANT SUNDAY CLASS'
res=''
ss=''
for i in s:
    if i!=' ':
        ss+=i

    else:
        res=' '+ss+res
        ss=''
res=ss+res
print(res)
        
