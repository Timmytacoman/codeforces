n = int(input())
t = 0
minimum = 0
for i in range(n):
    l, e = input().split()
    l = int(l)
    e = int(e)
    t += (e - l)
    if t > minimum:
        minimum = t
print(minimum)
