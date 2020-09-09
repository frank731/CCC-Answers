j_num, a_num = int(input()), int(input())
count = 0
jerseys = []
mapping = {"S": 1, "M": 2, "L": 3}
for i in range(j_num):
    jerseys.append(mapping[input()])

for i in range(a_num):
    a = input().split()
    index = int(a[1]) - 1
    size = jerseys[index]
    if mapping[a[0]] <= size:
        count += 1
        jerseys[index] = 0

print(count)



