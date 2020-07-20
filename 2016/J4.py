start = int(''.join(input().split(":")))
distcovered = 0
dist = 120

while distcovered < dist:
    if (start + 1) % 100 == 60:
        start = start - (start % 100) + 100
        if start + 1 >= 2500:
            start = 100
    else:
        start += 1
    if 700 < start < 1000 or 1500 < start < 1900:
        distcovered += 0.5
    else:
        distcovered += 1

if start == 2400:
    print("00:00")
else:
    if start >= 1000:
        print(str(start)[:2] + ":" + str(start)[2:])
    else:
        print("0" + str(start)[0] + ":" + str(start)[1:])
