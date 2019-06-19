numVowels = 0
for letter in s:
    if letter in ("a", "e", "i", "o", "u"):
        numVowels += 1
print("Number of vowels: "+ str(numVowels))