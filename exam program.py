s = '2IS EXA3M QUESTIO4N TH1IS'
d={}
for i in s.split():
    num=''
    ss=''
    for j in i:
        
        if '0'<=j<='9':
            num+=j
        else:
            ss+=j
    d[int(num)]=ss
t=list(d.keys())
t.sort()
a=''
for i in t:
    a+=d[i]+' '
print(a.strip())

