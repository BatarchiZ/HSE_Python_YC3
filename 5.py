list = list(map(int, (input().split())))
new_list = []
for x, y, z in zip(list, list[1:], list[2:]):
    if y > x and y > z:
        new_list.append(y)
print(len(new_list))
