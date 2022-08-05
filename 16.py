list_ = list(map(int, input().split()))
x, y = input().split()
list_.insert(int(x), int(y))
for i in list_:
    print(i)
