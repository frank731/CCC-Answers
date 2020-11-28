word = input()
usable = ["I", "O", "S", "H", "Z", "X", "N"]
works = True

for i in word:
    if i not in usable:
        print("NO")
        works = False
        break

if works:
    print("YES")