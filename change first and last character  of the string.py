s='student are more lazy'
l=s.split()
a=[]
for i in l:
    b=i[::-1]
    a.append(b)

c=' '.join(a)
print(c)
print('\n')
#-----------------------------------------------------------------------------------

s='student are more lazy'
l=s.split()
a=[]
for i in l:
    if len(i)>1:
        b=i[-1]+i[1:-1]+i[0]
        a.append(b)
    else:
        a.append(i)
c=' '.join(a)
print(c)
print('\n')
#-----------------------------------------------------------------------------------
s = 'student are more lazy'
l = s.split()  # Split the string into a list of words
a = []  # Create an empty list to store the modified words

# Iterate over each word in the list
for i in l:
    if len(i) > 1:  # Check if the word has more than one character
        b = i[-1] + i[1:-1] + i[0]  # Reverse the order of the first and last characters
        a.append(b)  # Add the modified word to the list
    else:
        a.append(i)  # If the word has only one character, add it as it is

c = ' '.join(a)  # Join the modified words back into a single string
print(c)
