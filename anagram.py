s1='Mother In Law'
s2='Hitler Woman'
s1=s1.replace(' ','').upper()
s2=s2.replace(' ','').upper()
if len(s1)!=len(s2):
    print('not anagram')
for i in s1:
    if s1.count(i)!=s2.count(i):
        print('not amagram')
        break
else:
    print('angram')
print('\n')
#--------------------------------------------------------------------------------

s1='Mother In Law'
s2='Hitler Woman'
if sorted(s1)==sorted(s2):
    print('anagram')
else:
    print('not anagam')
