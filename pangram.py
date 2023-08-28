s='The quick brown fox jumps over a lazy dog'
s=s.split()
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in s:
        print('not panagram')
        break
else:
    print('panagram')
