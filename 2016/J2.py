grid = []
for i in range(4):
    grid.append([int(i) for i in input().split()])

need = sum(grid[0])
magic = True
for row in grid:
    if sum(row) != need:
        print("not magic")
        magic = False
        break
if magic:
    for i in range(4):
        if grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i] != need:
            magic = False
            print("not magic")
            break

if magic:
    print("magic")
