s='shashi'
a=''
for i in range(-1,-len(s)-1,-1):
    a+=s[i]
if a==s:
    print('pali')
else:
    print('not')
#-------------------------------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
for i in range(0,len(s)//2):
    if s[i]!=s[-i-1]:
        print('not palindrome')
        break
else:
    print('palindrome')
#-------------------------------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        print('not')
        break
else:
    print('pali')
