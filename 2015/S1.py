count = int(input())
numbers = []
for i in range(count):
    num = int(input())
    if num == 0:
        del numbers[-1]
    else:
        numbers.append(num)

print(sum(numbers))