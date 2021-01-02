first = input().split()
second = input().split()
score = int(second[int(first[1]) - 1])
counter = 0
for i in second:
    if int(i) >= score and int(i) != 0:
        counter += 1
print(counter)
