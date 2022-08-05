list_ = list(map(int, input().split()))
Remove = int(input())
list_.pop(Remove)

for i in list_:
    print(i)
