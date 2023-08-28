s = 'gym is located on top of sky bar'
l = s.split()
vo = 'aeiouAEIOU'
vowel_words = []
for word in l:
    for char in word:
        if char in vo:
            vowel_words.append(word)
            break

print("Vowel words: " + ' '.join(vowel_words))

#---------------------------------------------------------------------------------------------------------------
print('\n')

s = 'gym is located on top of sky bar'
l = s.split()
vo = 'aeiouAEIOU'
a=''
for i in l:
    for j in i:
        if j in vo:
         print(i)
         break
print(' '.join(a))
#---------------------------------------------------------------------------------------------------------------
print('\n')
s = 'gym is located on top of sky bar'
l = s.split()
vo = 'aeiouAEIOU'
for i in l:
    for j in i:
        if j   in vo:
         print(j)
         break
#---------------------------------------------------------------------------------------------------------------
print('\n')
s = 'gym is located on top of sky bar'
l = s.split()
vo = 'aeiouAEIOU'
for i in l:
    for j in i:
        if j  in vo:
            break
    else:
        print(i)
#---------------------------------------------------------------------------------------------------------------
print('\n')
s = 'gym is located on top of sky bar'
l = s.split()
vo = 'aeiouAEIOU'
a=[]
for i in l:
    for j in i:
        if j  in vo:
            break
    else:
        a.append(i)
print(' '.join(a))



