text = input("Enter Input:")

ascii_values = []

for character in text:
    ascii_values.append(ord(character))
hex_values = [hex(x) for x in ascii_values]

print("Text: ", text)
print("Dec: ", ascii_values)
print("Hex: ", hex_values)

splitedSize = 4
hex_splited = [hex_values[x:x+splitedSize] for x in range(0, len(hex_values), splitedSize)]

print("Splitted into 4 Byte: ", hex_splited)
