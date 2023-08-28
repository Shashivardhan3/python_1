s='mnopq'
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
       print(s[i:j])
\
print('\n')
#-----------------------------------------------------------------------------------------
s='shashi'
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if(s[i:j]==s[i:j][::-1]):
            
        
        
            
            print(s[i:j])

print('\n')
#-----------------------------------------------------------------------------------------


s = 'shashi'

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substr = s[i:j]
        if substr == substr[::-1]:
            print(substr)
            
print('\n')
#-----------------------------------------------------------------------------------------
s='this text contains deed level to understand malayalam words for noon'
l=s.split()
for i in l:
    if i == i[::-1]:
        print(i)

print('\n')
#-----------------------------------------------------------------------------------------
s='this text contains deed level to understand malayalam words for noon'
l=s.split()
a=[]
for i in l:
    if i != i[::-1]:
        a.append(i)
print(' '.join(a))
#-----------------------------------------------------------------------------------------
s='this text contains deed level to understand malayalam words for noon'
l=s.split()
r=''
for i in l:
    if i != i[::-1]:
        r+=i+' '
print(r.strip())
        



