 l=[11,12,19,21,27]
for i in range(0,len(l)):
    if i%2==0:
        print(l[i])
print('\n')
#-------------------------------------------------------------------------------
l=[11,12,19,21,27]
for i in range(1,len(l)):
    if i%2!=0:
        print(l[i])
print('\n')
print('\n')
#-------------------------------------------------------------------------------
l=[11,12,19,21,27,23]
for i in range(0,len(l)//2):
    print(l[i])
print('\n')
#-------------------------------------------------------------------------------
l=[11,12,19,21,27,23]
for i in range(len(l)//2,len(l)):
    print(l[i])
