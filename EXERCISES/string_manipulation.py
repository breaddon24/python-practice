def count_vowels(s):
    output = 0
    vowels = 'aeiou'

    for char in s:
        for i in char:
            if i in vowels:
                output += 1
    return output

print(count_vowels("education"))

def modify(text: str, chosen_letter: str, replace: str):

    for char in text:
        for c in char:
            if c == chosen_letter:
                text = text.replace(c, replace)
    return text
print(modify("banana", "a", "*"))

for word in words:
    for index in indices:
        print(word[index], end=' ')
    print()

letters = ["U", "S", "Y", "D"]
for i in range(4):
    print(letters[3 - i], end=' ')