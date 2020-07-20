from string import ascii_lowercase
s = input()
slen = len(ascii_lowercase) - 1
nearest_vowel = {}
nearest_consan = {"z" : "z"}
letters = list(ascii_lowercase)
vowels = "aeiou"
new = ""
for i in s:
    if i not in vowels:
        new += i
        if i not in nearest_vowel:
            start = letters.index(i)
            index = 1
            found = False
            while not found:
                if start - index >= 0:
                    if letters[start - index] in vowels:
                        new += letters[start - index]
                        nearest_vowel[i] = letters[start - index]
                        found = True
                        break
                if start + index <= slen:
                    if letters[start + index] in vowels:
                        new += letters[start + index]
                        nearest_vowel[i] = letters[start + index]
                        found = True
                        break
                index += 1
        else:
            new += nearest_vowel[i]

        if i not in nearest_consan:
            start = letters.index(i)
            index = 1
            found = False
            while not found:
                if letters[start + index] not in vowels:
                    found = True
                    new += letters[start + index]
                    nearest_consan[i] = letters[start + index]
                    break
                index += 1
        else:
            new += nearest_consan[i]
    else:
        new += i

print(new)
