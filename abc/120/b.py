import sys
input = sys.stdin.readline
limit = 1000
A, B, K = map(int, input().split())
if A > B:
    max_num = A
else:
    max_num = B
li = []
for i in range(1, limit):
    if A%i == 0 and B%i == 0:
        li.append(i)

li.reverse()
print(li[K-1])
