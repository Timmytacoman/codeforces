n = int(input())
counter = 0
for i in range(n):
    line = input()
    total = int(line[0]) + int(line[2]) + int(line[4])
    if total >= 2:
        counter += 1
print(counter)
