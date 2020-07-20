q = input()
w = input()
e = input()
r = input()

an = True
if q == "8" or q == "9":
    if r == "8" or r == "9":
        if w == e:
            print("ignore")
            an = False

if an:
    print("answer")
