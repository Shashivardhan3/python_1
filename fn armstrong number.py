def armstrong(n,p):
    add=0
    while n!=0:
        rem=n%10
        add+=rem**p
        n//=10
        
    return add
n=153
p=(len(str(n)))
if n==armstrong(n,p):
        print('arm')
else:
    print('not arm')
