counter = 0
list_ = list(map(int, input().split()))
for i in range(len(list_)):
    for z in range(i + 1, len(list_)):
        if list_[i] == list_[z]:
            counter = counter + 1
print(counter)
