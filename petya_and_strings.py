first = input()
first = first.lower()
second = input()
second = second.lower()
if first < second:
    print("-1")
elif second < first:
    print("1")
else:
    print("0")