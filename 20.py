a = list(map(int, input().split()))

count = 0
for i in a:
    if i != 0:
        print(i, end=" ")
    else:
        count += 1
print("0 " * count)
