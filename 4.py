list = list(map(int, (input().split())))
new_list = []
for x, y in zip(list, list[1:]):
    if (y > 0 and x > 0) or (y < 0 and x < 0):
        if len(new_list) < 2:
            new_list.append(x)
            new_list.append(y)

for i in new_list:
    print(i)
