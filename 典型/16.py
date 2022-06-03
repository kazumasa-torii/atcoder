import sys
input = sys.stdin.readline
size = 10000
limit = int(input())
A, B, C = map(int, input().split())
ans = 100000
for i in range(size):
    if A * i > limit:
        break
    for j in range(size):
        if A * i + B * j > limit:
            break
        c = (limit - (A * i + B * j)) / C
        if c.is_integer():
            ans = min(ans, i + j + c)
print(int(ans))
