list_ = list(map(int, input().split()))
for i in range(1, len(list_), 2):
    j = (i - 1)
    x = list_[i]
    list_[i] = list_[j]
    list_[j] = x
for i in list_:
    print(i)
