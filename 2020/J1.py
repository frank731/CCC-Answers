import sys
small = int(input())
mid = int(input())
large = int(input())
score = small + (mid * 2) + (large * 3)
if score >= 10:
    print("happy")
else:
    print("sad")
