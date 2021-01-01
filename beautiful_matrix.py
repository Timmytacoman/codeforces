row = 0
col = 0
for i in range(5):
    line = ''.join(input().split())
    col = line.find("1")
    if col != -1:
        row = i + 1
        diffx = abs(3 - (col + 1))
        diffy = abs(3 - row)
        print(diffx + diffy)
