import math

line = input().split()
first_num = int(line[0])
second_num = int(line[1])
product = first_num * second_num
answer = product / 2
print(math.floor(answer))
