gates_count = int(input())
planes_count = int(input())
planes = []
docked = [False] * gates_count

for i in range(planes_count):
    planes.append(int(input()))

for i in range(planes_count):
    plane = planes[i] - 1
    if docked[plane]:
        while docked[plane]:
            plane -= 1
            if plane == -1:
                break
    if plane == -1:
        print(i)
        break
    docked[plane] = True
