import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(input())
li = []
index = 0
for i in range(0, len(A)):
    if A[i-1] == 'A' and A[i] == 'C':
        index += 1
        li.append(index)
    else:
        li.append(index)

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = li[y]
    ans -= li[x]
    print(ans)
