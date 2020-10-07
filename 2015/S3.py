gates_count = int(input())
planes_count = int(input())
planes = []
seen = {}
fitted = 1


for i in range(planes_count):
    planes.append(int(input()))

planes.sort(reverse=True)

largest = planes[0]

for plane in planes[1:]:
    if plane > largest:
        largest -= 1
        fitted += 1

print(fitted)
