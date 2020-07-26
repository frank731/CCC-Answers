count = int(input())
messages = []
friends = {}
friendswaittime = {}
noreply = {}
time = 0
for i in range(count):
    messages.append(input().split())

for i in messages:
    friendnum = int(i[1])
    typemessage = i[0]
    if typemessage == "W":
        time += friendnum - 1
    else:
        if friendnum not in friendswaittime:
            friendswaittime[friendnum] = 0
        if typemessage == "R":
            friends[friendnum] = time
            noreply[friendnum] = True
        elif typemessage == "S":
            friendswaittime[friendnum] += time - friends[friendnum]
            noreply[friendnum] = False
        time += 1

for i in sorted(friendswaittime.keys()):
    if not noreply[i]:
        print(i, friendswaittime[i])
    else:
        print(i, -1)



