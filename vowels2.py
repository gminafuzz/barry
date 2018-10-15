vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
word = input()

for letter in word:
    if letter in vowels:
        vowels[letter] += 1

for i in vowels:
    print (i, 'was found', vowels[i], 'time(s)')
