vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for vow in vowels:
    found[vow] = 0
for letter in word:
    if letter in found:
        found[letter] += 1
for i, j in sorted(found.items()):
    print (i, 'was found', j, 'time(s')
