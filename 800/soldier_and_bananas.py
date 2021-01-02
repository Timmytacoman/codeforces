k, n, w = input().split()
total = 0
for i in range(1, int(w) + 1):
    total += int(k) * i
owed = int(n) - total
if owed < 0:
    print(abs(owed))
else:
    print(0)
