s = input()

sadcount = s.count(":-(")
happycount = s.count(":-)")

if sadcount == 0 and happycount == 0:
    print("none")
elif sadcount == happycount:
    print("unsure")
elif happycount > sadcount:
    print("happy")
else:
    print("sad")
