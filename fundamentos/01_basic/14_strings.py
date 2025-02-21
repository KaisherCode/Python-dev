# Strings

text = 'She knows Python programing'
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
    print('You chose well!!')
else:
    print('You also chose well')

size = len(text)
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('She'))
print(text.endswith('Rust'))
print(text.replace('Python','Go'))

text_2 = 'This is a title'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("234".isdigit())