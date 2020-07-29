#goes over memory on last few cases

res_num, pho_num = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
stack = [p[0]]
p = {x: True for x in p}
graph = {}
for i in range(res_num - 1):
    temp = [int(x) for x in input().split()]
    if temp[0] not in graph:
        graph[temp[0]] = [temp[1]]
    else:
        graph[temp[0]].append(temp[1])

    if temp[1] not in graph:
        graph[temp[1]] = [temp[0]]
    else:
        graph[temp[1]].append(temp[0])


seen = {stack[0]: True}
used = {}
subtree = {}
distances = {stack[0]: 0}
while stack:
    item = stack.pop(-1)
    if item not in subtree:
        subtree[item] = [item]
    for n in graph[item]:
        if n not in seen:
            subtree[n] = subtree[item] + [n]
            seen[n] = True
            stack.append(n)
            if n in distances and distances[n] > distances[item] + 1:
                distances[n] = distances[item] + 1
            elif n not in distances:
                distances[n] = distances[item] + 1
        if n in p:
            for i in subtree[n]:
                used[i] = True


farthest_pho = [0, 0]
seen_pho_count = 0
roads = 0
for i in distances:
    if i in p and distances[i] > farthest_pho[1]:
        farthest_pho = [i, distances[i]]

del subtree
del distances
del seen
stack = [farthest_pho[0]]
seen = {stack[0]: True}
distances2 = {stack[0]: 0}
farthest_pho2 = [0, 0]
while stack:
    item = stack.pop(-1)
    for n in graph[item]:
        if n not in seen and n in used:
            seen[n] = True
            stack.append(n)
            if n in distances2 and distances2[n] > distances2[item] + 1:
                distances2[n] = distances2[item] + 1
            elif n not in distances2:
                distances2[n] = distances2[item] + 1
            if n in p:
                if distances2[n] > farthest_pho2[1]:
                    farthest_pho2 = [n, distances2[n]]
used_len = len(used) - 1
print(farthest_pho2[1] + (used_len - farthest_pho2[1]) * 2)




