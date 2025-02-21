# Indexing

text = "She knows Python"
print(text[0])
print(text[1])

size = len(text)
print('size: ', size)
print(text[size-1])
print(text[-1])

# Slicing
print(f"[0:5] =>",text[0:5])
print(f"[10:16]=>",text[10:16])
print(f"[:10]=>",text[:10])
print(f"[5:-1]=>",text[5:-1])
print(f"[5:]=>",text[5:])
print(f"[:]=>",text[:])
print(f"[10:16:1]=>",text[10:16:1])
print(f"[10:16:2]=>",text[10:16:2])
print(f"[::2]=>",text[::2])