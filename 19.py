NK = list(map(int, input().split()))
N = NK[0]
K = NK[-1]
x = int(NK[-1])
list_ = []
while x != 0:
    list1 = list(map(int, input().split()))
    y = list(range(list1[0], list1[1] + 1))
    list_ = list_ + y
    x = x - 1

pinslist = ['I'] * N

for a in list_:
    pinslist[a - 1] = '.'
str1 = ''.join(pinslist)
print(str1)
