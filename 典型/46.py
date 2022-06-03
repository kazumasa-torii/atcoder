import numbers
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def solve(index, tmp):
    if index == 3:
        if tmp == 0:
            ans += 1
        return
    for i in nums[index]:
        solve(index+1, (tmp + i) % num)

num = 46
ans = 0
N = int(input())
nums = [[] for _ in range(3)]
tmp = []
for i  in range(3):
    tmp = list(map(int, input().split()))
    for j in tmp:
        nums[i].append(j % num)


solve(0, 0)
print(ans)
