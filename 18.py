list_ = list(map(int, input().split()))
list = []
for i in list_:
    if list_.count(i) == 1:
        list.append(i)

for i in list:
    print(i)
