n=8
cb=n**3
while n!=0:
    r1=n%10
    r2=cb%10
    if r1!=r2:
        print('not trophic')
        break
    n//=10
    cb//=10
else:
    print('tri morphic')
