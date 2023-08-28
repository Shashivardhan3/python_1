s='aaaabbcccddda'
c=1
res=''
for i in range (0,len(s)-1):
    
    if s[i] == s[i+1]:
        c+=1
    else:
        res+=str(c)+s[i]
        c=1
res+=str(c)+s[-1]
print(res)
#---------------------------------------------------------------------------------
print('\n')
s='yycbbbyyyy'
mc,c,ss=0,1,''
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        if mc>c:
            mc = c
    else:
        ss+=s[i]*mc
        c=1
ss+=s[i]*mc
print(ss)
 
s = 'yyccccccbbbyyyyyyyyyyyyy'
mc, c, ss = 0, 1, ''
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
        if mc < c:
            mc = c
            ss = s[i] * mc
    else:
        c = 1

print(ss)
 #---------------------------------------------------------------------------------
print('\n')  
s = 'yycccccbbbbbbbbbbbbbbyyyy'
mc, c, ss= 0, 1, ''
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        if mc<c:
            
            mc=c
            ss=s[i]*c
        c=1
if mc<c:
    mc=c
    ss=s[i]*c
print(ss)

































