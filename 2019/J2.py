l = int(input())
encode = []
for i in range(l):
    encode.append(input().split())
for i in encode:
    temp = ""
    for o in range(int(i[0])):
        temp += i[1]
    print(temp)
