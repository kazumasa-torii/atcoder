import sys
input = sys.stdin.readline
S = list(input())
K = int(input())
ans = 0
for i in S:
    if i == 1:
        if K == 1:
            ans = 1
            break
        continue
    ans = i
    break
print(ans)
