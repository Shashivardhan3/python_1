s='shashiSHAHSI@123'
a=''
for i in s:
    if 'A'<=i<='Z':
        a+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        a+=chr(ord(i)-32)
    else:
        a+=i
print(a)
