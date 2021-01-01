lines = int(input())
total = 0
for i in range(lines):
    line = input()
    if '+' in line:
        total += 1
    else:
        total -= 1
print(total)