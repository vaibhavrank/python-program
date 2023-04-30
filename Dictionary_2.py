str = input("Enter the string:")

char_frequency = {}

for char in str:
    if char.isspace():
        continue

    if char in char_frequency:
        char_frequency[char] += 1
    else :
        char_frequency[char] = 1


for char,frequency in char_frequency.items():
    print(f"'{char}': {frequency}")