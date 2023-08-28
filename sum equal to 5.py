s = [2, 4, 3, 7, 1]
for i in range(0, len(s)-1):
    
    for j in range(i+1, len(s)):
        
        if s[i] + s[j] == 5:
            print((s[i], s[j]))
print('\n')
#---------------------------------------------------------------------------------

s = [1, 5, 2, 7, 4, 0, 3]
m=11
n=7
for i in range(0, n):
    for j in range(i + 1, n+1):
        if sum(s[i:j]) ==  m:
            print(s[i:j])

print('\n')
#---------------------------------------------------------------------------------
s=[1,5,2,3,7,4,0,3]
m=11
n=8
for i in range(0,n):
    for j in range(i+1,n+1):
        a=0
        for k in s[i:j]:
            a+=k
        if a==m:
            print(s[i:j])

print('\n')
#---------------------------------------------------------------------------------
s=[1,5,2,7,4,0,3]
m=11
n=7
for i in range(0,n):
    for j in range(i+1,n+1):
        sum=0
        for k in range(i,j):
            
            sum+=s[k]
        if sum==m:
            print(s[i:j])
print('\n')
#---------------------------------------------------------------------------------
s=[1,5,2,7,4,0,3]
m=11
n=7
for i in range(0,n):
    for j in range(i+1,n+1):
        l=[]
        for k in range(i,j):
            l.append(s[k])
        print(l)




















        
