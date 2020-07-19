flips = input()
trueflips = ""
if flips.count("H") % 2 == 1:
    trueflips += "H"
if flips.count("V") % 2 == 1:
    trueflips += "V"

if trueflips == "H":
    print("3 4")
    print("1 2")
elif trueflips == "V":
    print("2 1")
    print("4 3")
elif trueflips == "HV":
    print("4 3")
    print("2 1")
else:
    print("1 2")
    print("3 4")
