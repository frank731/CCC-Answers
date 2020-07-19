totala = 0
totalb = 0
for i in reversed(range(1, 4)):
    totala += int(input()) * i
for i in reversed(range(1, 4)):
    totalb += int(input()) * i
if totala > totalb:
    print("A")
elif totalb > totala:
    print("B")
else:
    print("T")
