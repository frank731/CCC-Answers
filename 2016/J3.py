s = input()

index = len(s)

found = False
for i in reversed(range(index)):
    for o in range(index - i):
        cut = s[o:i + o + 1]
        if cut == cut[::-1]:
            print(i + 1)
            found = True
            break
    if found:
        break
