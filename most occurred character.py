s='shasdddhi'
a=0
for i in s:
    if s.count(i)>a:
        a=s.count(i)
b=''
for i in s:
    if s.count(i)==a and i not in b:
        print(i)
        b+=i
