s='SHAHSI'
a=''
for i in s:
    if  'A'<=i<='Z':
        a+=chr(ord(i)+32)
    else:
        a+=i
print(a)
#-----------------------------------------------------------------------------------------------------------------
print('\n')

s = 'SHAHSI'
a = s.lower()
print(a)
#-----------------------------------------------------------------------------------------------------------------
print('\n')
s = 'SHAHSI'
a = s.islower()
print(a)
