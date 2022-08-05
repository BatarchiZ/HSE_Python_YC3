list_ = list(map(int, input().split()))
tuple_ = tuple(list_)
for i in range(len(list_)):
    list_[i] = tuple_[i - 1]
for i in list_:
    print(i)
