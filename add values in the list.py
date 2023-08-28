s=[12,79,152,126,51]
add=[]
for i in s:
    a=0
    while i!=0:
        rem=i%10
        a+=rem
        i//=10
    add.append(a)
print(add)
print('\n')#
#-----------------------------------------------------------------------------------------
def add(n):
    if n==0:
        return 0
    return n%10+add(n//10)
s=[12,79,152,126,51]
a=list(map(add,s))
print(a)
print('\n')#
#-----------------------------------------------------------------------------------------
def add(n):
    if n==0:
        return 0
    return n%10+add(n//10)
s=[12,79,152,126,51]
for i  in range(len(s)):
    s[i]=add(s[i])
print(s)
