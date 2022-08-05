list = list(map(int, (input().split())))
new_list = []
for i in list:
    if i > 0:
        new_list.append(i)
ordered_list = sorted(new_list)
print(ordered_list[0])
