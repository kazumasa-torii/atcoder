import sys
input = sys.stdin.readline
size = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans= 0
for i in range(size):
    ans += abs(a[i] - b[i])
print(ans)
