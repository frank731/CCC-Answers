string = input()
sub = input()
subs = []
printno = True
for i in sub:
    subs.append(sub)
    sub += sub[0]
    sub = sub[1:]
for sub in subs:
    if string.find(sub) != -1:
        print("yes")
        printno = False
        break
if printno == True:
    print("no")
