s='student are more lazy'
l=s.split()
nl=[]
for i in l:
    a=list(i)
    a[0],a[-1]=a[-1],a[0]
    nl.append(''.join(a))
print(' '.join(nl))
