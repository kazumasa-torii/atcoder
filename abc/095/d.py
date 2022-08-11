import sys
input = sys.stdin.readline
N, C = map(int, input().split())
nums = []
tmp = 0
for _ in range(N):
    x, y = map(int, input().split())
    tmp += y
    nums.append([x, tmp-x])
nums = sorted(nums, key=lambda x: x[1])
print(nums[-1][1])
