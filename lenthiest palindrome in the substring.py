s='this text contains malayalam words for noon racecar and level'

b=s.split()
a=[]
h=0
for i in b:
    if i==i[::-1]:
        
        a.append(i)
        if  h<len(i):
            h=len(i)
for i in a:
    if len(i)==h:
        print(i)
print('\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------
s='ababcb'
l=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        ss=s[i:j]
        if ss == ss[::-1]:
            l.append(ss)
h=0
for i in l:
    if h<len(i):
        h=len(i)
for i in l:
    if h==len(i):
        print(i)
