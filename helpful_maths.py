line = input()
nums = []
for i in line:
    try:
        nums.append(int(i))
    except:
        pass
nums.sort()
new_nums = []
for i in nums:
    new_nums.append(str(i))
if len(nums) == 1:
    print(nums[0])
else:
    word = ""
    for i in new_nums:
        word += i + "+"
    print(word[:-1])
