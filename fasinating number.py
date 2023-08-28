n=320
a=str(n*1)
b=str(n*2)
c=str(n*3)
d=a+b+c
for i in range(1,10):
    if str(i) not in d:
        print('not fasinating')
        break
else:
    print('fasinating')
        
