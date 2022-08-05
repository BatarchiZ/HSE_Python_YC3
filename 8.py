list = list(map(int, (input().split())))
peter = int(input())
order_list = sorted(list)
counter = 1
for i in list:
    if peter <= i:
        counter = counter + 1
print(counter)
