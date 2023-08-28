'''
 s='AD4C5FE96'
 o/p:EF4C5DA96
'''

s = 'AD4C5FE96'
a=s[:2] 
b=s[2:8]
print(b[::-1])
c=s[8:]
d=b[::-1]
d=d[-1]+d[1:-1]+d[0]
res= a+d+c 

print(res)

''''
s = 'AD4C5FE96'

# Separate the string into two parts
first_part = s[:2]  # 'AD'
middle_part = s[2:8]  # '4C5FE9'
last_part = s[8:]  # '6'

# Reverse the middle part
reversed_middle_part = middle_part[::-1]  # '9E5C4C'

# Swap the first and last characters of the reversed middle part
reversed_middle_part = reversed_middle_part[-1] + reversed_middle_part[1:-1] + reversed_middle_part[0]  # '9C5E4C'

# Concatenate the parts in the desired order
output = first_part + reversed_middle_part + last_part  # 'EF4C5DA96'

print(output)


reversed_middle_part[-1]: This retrieves the last character of the string reversed_middle_part. In this case, it is '9'.

reversed_middle_part[1:-1]: This retrieves the portion of the string reversed_middle_part starting from the second character (reversed_middle_part[1]) up to, but not including, the last character (reversed_middle_part[-1]). This effectively excludes the first and last characters from the middle part. In this case, it is 'C5E4'.



reversed_middle_part[0]: This retrieves the first character of the string reversed_middle_part. In this case, it is 'C'.



s = 'AD4C5FE96'

# Convert the string to a list of characters
chars = list(s)

# Swap specific characters at their respective indices
chars[0], chars[1] = chars[1], chars[0]  # Swap 'A' and 'D'
chars[2], chars[7] = chars[7], chars[2]  # Swap '4' and 'E'
chars[3], chars[6] = chars[6], chars[3]  # Swap 'C' and '5'

# Convert the list back to a string
output = ''.join(chars)

print(output)
'''


s = 'yycbbbyyyy'

current_char = None
current_count = 0
max_char = None
max_count = 0

for char in s:
    if char == current_char:
        current_count += 1
    else:
        current_char = char
        current_count = 1
    if current_count > max_count:
        max_char = current_char
        max_count = current_count

output = f'{max_char}={max_count}'

print(output)
