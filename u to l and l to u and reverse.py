s='SHAHSHI vardhan'
a=s.swapcase()
for i in range(-1,-len(s)-1,-1):
    print(a[i],end ='')


    
s = 'SHAHSHI vardhan'
a = ''

for i in s:
    if 'A'<=i<='Z':
        a+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        a+=chr(ord(i)-32)
    else:
        a+=i

for i in range(-1, -len(a)-1, -1):
    print(a[i], end='')
