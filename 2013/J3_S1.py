year = int(input())

year += 1
year = str(year)

while len(set(year)) != len(year):
    year = str(int(year) + 1)

print(year)