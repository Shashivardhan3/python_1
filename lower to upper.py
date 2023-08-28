s='shashi'
a=''
for i in s:
    if 'a'<=i<='z':
        a+=chr(ord(i)-32)
    else:
        a+=i
print(a)
#--------------------------------------------------------------------------------------------------
print('\n')
s='shashi'
print(s.upper())
