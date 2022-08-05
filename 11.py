list_ = list(map(int, input().split()))
list1 = tuple(list_)
for i in range((len(list_))):
    j = -(i + 1)
    list_[i] = list1[j]
for i in list_:
    print(i)
