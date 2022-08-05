list = list(map(int, (input().split())))
new_list = []
new_list.append(list[0])
for i in list:
    if i not in new_list:
        new_list.append(i)
print(len(new_list))
