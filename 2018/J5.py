from math import inf

graph = {}

class Node:
    def __init__(self, children, number):
        self.children = children
        self.distance = inf
        self.parents = []
        self.number = number
    def get_number(self):
        return self.number
    def get_children(self):
        if self.children == [0]:
            return 0
        else:
            return self.children[1:]
    def get_distance(self):
        return self.distance
    def set_distance(self, past):
        self.distance = past + 1
    def get_parents(self):
        return self.parents
    def add_parents(self, parent):
        self.parents.append(parent)


pagecount = int(input())
for i in range(pagecount):
    graph[i + 1] = Node([int(x) for x in input().split()], i + 1)


graph[1].set_distance(0)

graph[1].parents = ["root"]

queue = [graph[1]]

seen = {}

for i in graph:
    seen[i] = False

shortestpath = inf

while queue:
    i = queue.pop(0)
    if not seen[i.get_number()]:
        seen[i.get_number()] = True
        lchildren = i.get_children()
        if lchildren != 0:
            for o in lchildren:
                temp = graph[o]
                if temp.get_parents() != ["root"]:
                    temp.add_parents(i)
                    temp.set_distance(min([i.get_distance() for i in temp.get_parents()]))
                    queue.append(temp)
                    graph[o] = temp
        else:
            if i.get_distance() < shortestpath:
                shortestpath = i.get_distance()

printy = True

for i in seen.values():
    if not i:
        print("N")
        printy = False
        break

if printy:
    print("Y")

print(shortestpath)
