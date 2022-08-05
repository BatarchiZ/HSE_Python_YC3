list = list(map(int, (input().split())))
even_list = []
for i in list:
    if i % 2 == 0:
        even_list.append(i)
for i in even_list:
    print(i)
