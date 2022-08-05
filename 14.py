list_ = list(map(int, input().split()))
max_ = max(list_)
min_ = min(list_)
M = list_.index(max_)
L = list_.index(min_)
list_[M] = min_
list_[L] = max_

for i in list_:
    print(i)
