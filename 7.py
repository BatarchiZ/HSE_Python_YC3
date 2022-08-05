list = list(map(int, (input().split())))
new_list = []
for i in list:
    if i % 2 != 0:
        new_list.append(i)
ord_list = sorted(new_list)
print(ord_list[0])
