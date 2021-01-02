input()
row = ' '.join(input()).split(' ')
counter = 0


def remove_duplicates(given_row):
    global counter
    for i in range(len(given_row) - 1):
        if given_row[i] == given_row[i + 1]:
            given_row.pop(i)
            counter += 1
            remove_duplicates(given_row)
    print(counter)
    exit()


remove_duplicates(row)
