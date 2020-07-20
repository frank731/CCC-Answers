cities = [0]
for i in input().split():
    cities.append(cities[-1] + int(i))

for i in cities:
    temp = ""
    for o in cities:
        temp += str(abs(i - o)) + " "
    print(temp)
