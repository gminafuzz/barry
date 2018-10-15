vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
word = input()

for letter in word:
    if letter in vowels:
        vowels[letter] += 1

for i, j in sorted(vowels.items()):
    print (i, 'was found', j, 'time(s)')
