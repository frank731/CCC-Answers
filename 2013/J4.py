time = int(input())
tasks = int(input())
task_times = []
for i in range(tasks):
    task_times.append(int(input()))

task_times.sort()
index = 0

while time > 0:
    time -= task_times[index]
    index += 1

if time < 0:
    index -= 1
    
print(index)