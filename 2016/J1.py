s = 0
for i in range(6):
    if input() == "W":
        s += 1

if s >= 5:
    print("1")
elif s >= 3:
    print("2")
elif s >= 1:
    print("3")
else:
    print("-1")
