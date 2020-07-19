l = int(input())
encode = []
decode = []
for i in range(l):
    encode.append(input())
for i in encode:
    new = i[0]
    index = 0
    decoded = ""
    for o in i:
        if o == new:
            index += 1
        else:
            decoded += (str(index) + " " + new + " ")
            new = o
            index = 1
    decoded += (str(index) + " " + new + " ")
    decode.append(decoded)
for i in decode:
    print(i)
